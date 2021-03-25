from django.contrib.auth import get_user_model

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from apps.users.documents import UserDocument
from apps.users.helpers import SearchResults

from elasticsearch_dsl.query import Q

import graphene
from user_agents import parse

from apps.graphql_jwt import mixins
from apps.graphql_jwt.decorators import token_auth
from apps.graphql_jwt.refresh_token.utils import revoke_by_user

from apps.users.models import AccessData, User, UserProfile, GlobalSPFLID, PublicChangeLog, UserSettings
from apps.users.obj_types import UserType, UserProfileType

from apps.follows.models import Follow

from uuid import uuid4
import base64

from django.contrib.auth import logout
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


# make the mutations for updating a user and updating profile
# https://stackoverflow.com/questions/49084322/how-to-limit-field-access-on-a-model-based-on-user-type-on-graphene-django



class CustomJSONWebTokenMutation(mixins.ObtainJSONWebTokenMixin,
                           graphene.Mutation):
    class Meta:
        abstract = True

    @classmethod
    def Field(cls, *args, **kwargs):
        cls._meta.arguments.update({
            get_user_model().USERNAME_FIELD: graphene.String(required=True),
            'password': graphene.String(required=True),
        })
        return super(CustomJSONWebTokenMutation, cls).Field(*args, **kwargs)

    @classmethod
    @token_auth
    # @jwt_cookie
    def mutate(cls, root, info, **kwargs):
        user = info.context.user
        ip_addr_v4 = info.context.META['REMOTE_ADDR']
        ua_string = info.context.META['HTTP_USER_AGENT']
        user_agent = parse(ua_string)

        AccessData.objects.update_or_create(
            user=user, 
            defaults={
                'ip_addr_v4':ip_addr_v4, 'is_mobile':user_agent.is_mobile,
                'is_tablet':user_agent.is_tablet, 
                'is_touch_capable':user_agent.is_touch_capable,
                'is_pc':user_agent.is_pc, 'is_bot':user_agent.is_bot,
                'browser':user_agent.browser.family, 
                'browser_version':user_agent.browser.version_string,
                'os':user_agent.os.family, 
                'os_version':user_agent.os.version_string,
                'device':user_agent.device.family
            }
        )
        
        # push notifications device stuff
        # NOTE:
        # On frontend, do token management and get the token, store in global variable
        # in apollo middleware, if the path is /login, then append the reg_id as a request header
        # also send device_id for unqiue devie
        # here in backend, create new device and  UPDATE_ON_DUPLICATE_REG_ID will handle duplicate
        # or
        # check if device_id already exists, if so, check if reg_id is same. if same reg, ignore, 
                    # else update the reg_id 
        # if not, create new Device with reg_id and device_id and user, and name from ua, etc.

        return cls.resolve(root, info)

class CustomObtainJSONWebToken(mixins.ResolveMixin, CustomJSONWebTokenMutation):
    """Obtain JSON Web Token mutation"""

class Register(graphene.Mutation):
    """ Mutation to register a user """
    #user = graphene.Field(UserType)
    success = graphene.Boolean()
    #add proper errors lol
    errors = graphene.List(graphene.String)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        language = graphene.String(required=True)
        country = graphene.String(required=True)
        birthday = graphene.String(required=True)
        file = graphene.String(required=True)

    def mutate(self, info, username, email, password, first_name, last_name, language, country, birthday, file):
        if User.objects.filter(email__iexact=email).exists():
            errors = ['emailAlreadyExists']
            return Register(success=False, errors=errors)

        if User.objects.filter(username__iexact=username).exists():
            errors = ['usernameAlreadyExists']
            return Register(success=False, errors=errors)

        try:
            # create user
            user = User.objects.create(
                username=username,
                email=email,
                last_name=last_name,
                first_name=first_name,
                language=language,
                country=country,
                birthday=birthday
            )
            user.set_password(password)
            user.save()

            ### NOTE: remove fro prod: code to auto follow @memes
            # followee = User.objects.get(username='memes')
            # Follow.objects.add_follower(user, followee)

            # TODO: implement overlay/dialog for signout loading
            file_name = str(user.token)
            file_format, img_str = file.split(';base64,')
            file_ext = file_format.split('/')[-1] 
            file = default_storage.save(f'{file_name}.{file_ext}', ContentFile(base64.b64decode(img_str)))
            user.profile_pic = f'https://{settings.AWS_STORAGE_BUCKET_NAME}.{settings.AWS_S3_REGION_NAME}.cdn.digitaloceanspaces.com/{settings.MEDIAFILES_LOCATION}/{user.token}.jpeg'
            user.save()
        except:
            return Register(success=False, errors=['IntegrityError'])
            
        return Register(success=True) #user=user


class Logout(graphene.Mutation):
    """ Mutation to logout a user """
    success = graphene.Boolean()

    def mutate(self, info):
        logout(info.context)
        return Logout(success=True)


class ResetPassword(graphene.Mutation):
    """ Mutation for requesting a password reset email """
    # you can make ur own fields like this
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String(required=True)

    def mutate(self, info, email):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            errors = ['emailDoesNotExists']
            return ResetPassword(success=False, errors=errors)

        
        params = {
            'user': user,
            'DOMAIN': settings.DOMAIN,
        }
        
        send_mail(
            subject='Password reset',
            message=render_to_string('mail/password_reset.txt', params),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )
        return ResetPassword(success=True)


class ResetPasswordConfirm(graphene.Mutation):
    """ Mutation for requesting a password reset email """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        token = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, token, password):
        try:
            user = User.objects.get(token=token)
        except User.DoesNotExist:
            errors = ['wrongToken']
            return ResetPasswordConfirm(success=False, errors=errors)

        user.set_password(password)
        user.token = uuid4()
        user.save()
        return ResetPasswordConfirm(success=True)


### profile stuff
class AddView(graphene.Mutation):
    """ Mutation for adding 1 to the view count """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        username_viewee = graphene.String(required=True)

    def mutate(self, info, username_viewee):
        user = User.objects.get(username=username_viewee)
        profile = user.userprofile_set
        profile.view_count += 1
        profile.save()
        return AddView(success=True)


class Result(graphene.ObjectType):
    username = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()

class BasicSearch(graphene.Mutation):
    """ Mutation for executing a contains search for firstname, lastname, firstname """
    results = graphene.List(Result)
    errors = graphene.List(graphene.String)

    class Arguments:
        term = graphene.String(required=True)

    def mutate(self, info, term):
        if info.context.user.is_authenticated:
            search = UserDocument.search()
            q = Q(
                {
                    "multi_match": {
                        "query": term,
                        "fields": ['username^2', 'first_name^1.5', 'last_name^1'],
                        "fuzziness" : len(term) / 1.5, # adjust for prod
                        "prefix_length" : 1
                    }
                }
            )
            search = search.query(
                q
                # 'multi_match', query=term, fields=['username^2', 'first_name^1.5', 'last_name^1']
                # Q('match_phrase', username=term) |
                # Q('match_phrase', first_name=term) |
                # Q('match_phrase', last_name=term)
            )
            # for item in search:
            #     print(item.username)
            search_results = SearchResults(search)
            result_dict = [ { "username": i.username, "first_name": i.first_name, "last_name": i.last_name } for i in search_results ]
            end_results = []
            for d in result_dict:
                end_results.append(Result(d['username'], d['first_name'], d['last_name']))
            return BasicSearch(results=end_results)


class UpdateSPFLID(graphene.Mutation):
    """ Mutation for updating SPFL_ID variable from given parameter """
    success = graphene.Boolean()
    class Arguments:
        id = graphene.Int(required=True)
    def mutate(self, info, id):
        obj, created = GlobalSPFLID.objects.get_or_create(id=1)
        data = obj.spfl_id
        print(data)
        data.append(id)
        obj.spfl_id = data
        obj.save()

## EDITING USER PROFILE
class EditProfile(graphene.Mutation):
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:

        # link args
        changed = graphene.List(graphene.String, required=True)
        interest_tags = graphene.List(graphene.String, required=False)

        username = graphene.String(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        email = graphene.String(required=False)

        occupation = graphene.String(required=False)
        bio = graphene.String(required=False)
        education = graphene.String(required=False)
        location = graphene.String(required=False)
        website = graphene.String(required=False)
        contact_phone = graphene.String(required=False)
        contact_email = graphene.String(required=False)
        file = graphene.String(required=True)
        

    def mutate(self, info, username, changed, interest_tags='', email='', first_name='', last_name='',  occupation='', education='', location='', website='', bio='', contact_email='', contact_phone='', file=''):
        ### ADD A LAST TIME PROFILE WAS CHANGED VARIABLE
        ### DESCRIBE OTHER ANALYTICS VARIABLES
        
        erl = []
        if info.context.user.is_authenticated:
            user = info.context.user
            profile = user.profile
            changelog = []
            # put all in try catch lol

            if username and 'username' in changed:
                user.username = username
                changelog.append('username')

            ### NOTE: REMOVE EMAIL FROM EDITABLE FIELDS IN EDIT PROFILE!!
            if email and 'email' in changed:
                user.email = email

            if first_name and 'first_name' in changed:
                user.first_name = first_name

            if last_name and 'last_name' in changed:
                user.last_name = last_name

            if occupation and 'occupation' in changed:
                profile.occupation = occupation

            if education and 'education' in changed:
                profile.education = education

            if location and 'location' in changed:
                profile.location = location

            if website and 'website' in changed:
                profile.website = website
                changelog.append('website')

            if bio and 'bio' in changed:
                profile.bio = bio
                
            if contact_email and 'contact_email' in changed:
                profile.contact_email = contact_email
                changelog.append('contact email')

            if contact_phone and 'contact_phone' in changed:
                profile.contact_phone = contact_phone
                changelog.append('contact phone')
            
            if file and 'profile_pic' in changed:
                file_name = str(user.token)
                file_format, img_str = file.split(';base64,')
                file_ext = file_format.split('/')[-1] 
                default_storage.delete(f'{file_name}.{file_ext}')

                user.token = uuid4()
                
                file_name = str(user.token)
                file_format, img_str = file.split(';base64,')
                file_ext = file_format.split('/')[-1] 
                file = default_storage.save(f'{file_name}.{file_ext}', ContentFile(base64.b64decode(img_str)))
                user.profile_pic = f'https://{settings.AWS_STORAGE_BUCKET_NAME}.{settings.AWS_S3_REGION_NAME}.cdn.digitaloceanspaces.com/{settings.MEDIAFILES_LOCATION}/{user.token}.jpeg'
            
            #######

            if interest_tags:
                # print(interest_tags)
                try:
                    if len(interest_tags) > 0:
                        profile.interest_tags = interest_tags
                except:
                    erl.append('ListFormatError')
            else:
                erl.append('ListError')

            #######

            try:
                user.save()
                profile.save()
            except:
                erl.append('IntegrityError')

            try:
                for change in changelog:
                    PublicChangeLog.objects.create(user=user, service='', statement=f'changed their {change}')
            except:
                erl.append('IntegrityError')

            if len(erl) > 0:
                return EditProfile(success=False, errors=erl)

            return EditProfile(success=True)




class EditSettings(graphene.Mutation):
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        account_type = graphene.String(required=False)
        notifs_enable = graphene.Boolean(required=False)
        notifs_follows = graphene.Boolean(required=False)
        notifs_new_account = graphene.Boolean(required=False)
        notifs_updates = graphene.Boolean(required=False)
        sponsored_relevant = graphene.Boolean(required=False)
        privacy_accounts = graphene.String(required=False)
        privacy_follows = graphene.String(required=False)
        private_profile = graphene.Boolean(required=False)

    def mutate(self, info, **kwargs):
        ### NOTE: ADD A LAST TIME settings WAS CHANGED VARIABLE
        ### DESCRIBE OTHER ANALYTICS VARIABLES
        
        erl = []
        if info.context.user.is_authenticated:
            user = info.context.user
            settings = user.settings
            # put all in try catch lol
            # print('memes', kwargs['account_type'], kwargs['notifs_enable'], kwargs['notifs_follows'], kwargs['notifs_new_account'], kwargs['notifs_updates'], kwargs['sponsored_relevant'], kwargs['privacy_accounts'], kwargs['privacy_follows'], kwargs['private_profile'])
            if 'account_type' in kwargs:
                settings.account_type = kwargs['account_type']

            if 'notifs_enable' in kwargs:
                settings.notifs_enable = kwargs['notifs_enable']

            if 'notifs_follows' in kwargs:
                settings.notifs_follows = kwargs['notifs_follows']

            if 'notifs_new_account' in kwargs:
                settings.notifs_new_account = kwargs['notifs_new_account']

            if 'notifs_updates' in kwargs:
                settings.notifs_updates = kwargs['notifs_updates']

            if 'sponsored_relevant' in kwargs:
                settings.sponsored_relevant = kwargs['sponsored_relevant']

            if 'private_profile'in kwargs:
                settings.private_profile = kwargs['private_profile']

            if 'privacy_accounts' in kwargs:
                settings.privacy_accounts = kwargs['privacy_accounts']
                
            if 'privacy_follows' in kwargs:
                settings.privacy_follows = kwargs['privacy_follows']

            #######

            try:
                settings.save()
            except:
                erl.append('IntegrityError')

            if len(erl) > 0:
                return EditSettings(success=False, errors=erl)

            return EditSettings(success=True)


class SignOutAllDevices(graphene.Mutation):
    """ Mutation for signing out all of a user's devices """
    success = graphene.Boolean()

    def mutate(self, info):
        # NOTE: possibly change all is_authenticateds to @login_required deco
        if info.context.user.is_authenticated:
            try:
                revoke_by_user(info.context.user, info.context)
                return SignOutAllDevices(success=True)
            except:
                return SignOutAllDevices(success=False)