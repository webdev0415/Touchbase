import graphene
import json
from apps.links.models import ToushLink
from apps.links.obj_types import ToushLinkType
from apps.accounts.account_list import url_c_list

class CreateToushLink(graphene.Mutation):
    """ Mutation to make a toush link """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        max_count = graphene.Int(required=True)
        lifespan = graphene.Int(required=True)

        accounts_list = graphene.JSONString()

        custom_link = graphene.String(required=True)

        link = graphene.String(required=False) # string derived from url.
        link_to_profile = graphene.Boolean(required=False)
        is_toush_profile = graphene.Boolean(required=True)
        is_toush_feed = graphene.Boolean(required=True)
        is_toush_events = graphene.Boolean(required=True)
        username = graphene.Boolean(required=False)
        first_name = graphene.Boolean(required=False)
        last_name = graphene.Boolean(required=False)
        contact_phone = graphene.Boolean(required=False)
        #profile_picture = 
        #banner =
        #color scheme =
        contact_email = graphene.Boolean(required=False)
        message = graphene.String()

    def mutate(
        self, info, message, accounts_list, max_count=-1, lifespan=-1, link='touchbase.id/?redirect', link_to_profile=True, is_toush_events=False,
        is_toush_profile=False, is_toush_feed=False, username=False, first_name=False,
        last_name=False, contact_phone=False, contact_email=False, custom_link=''
    ):
        if info.context.user.is_authenticated:
            user = info.context.user
            ToushLink.objects.make_link( # returns m, so figure out how to use m or discard it
                user=user, link=link, max_count=max_count, lifespan=lifespan, link_to_profile=link_to_profile,
                is_toush_profile=is_toush_profile, is_toush_events=is_toush_events,
                is_toush_feed=is_toush_feed, username=username, first_name=first_name,
                last_name=last_name, contact_phone=contact_phone, contact_email=contact_email,
                message=message, custom_link=custom_link, accounts_list=accounts_list
            )
            return CreateToushLink(success=True)

        return CreateToushLink(success=False, errors=['notSignedIn'])

# class DeleteToushLink(graphene.Mutation):
#     success = graphene.Boolean()
#     errors = graphene.List(graphene.String)

#     class Arguments:
#         short_string = graphene.String(required=True)

#     def mutate(self, info, short_string): ### FIX THIS LOL
#         if info.context.user.is_authenticated:
#             user = info.context.user

#             ### TEST THE SPEED OF THIS AND THIS
#             #user.toush_links.get(toush_string__exact=short_string).toush_link.delete()
#             ToushLink.objects.get(short_url__exact=short_string).delete()

class DeleteToush(graphene.Mutation):
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        typeof = graphene.String(required=True)

        # account args
        identifier = graphene.String(required=False)
        service = graphene.String(required=False)

        # link args
        short_string = graphene.String(required=False)

    def mutate(self, info, typeof, identifier, service, short_string):
        erl = []
        if info.context.user.is_authenticated:
            user = info.context.user
# put all in try catch lol
            if typeof == 'link' and short_string:
                ### TEST THE SPEED OF THIS AND THIS - current is more secure
                user.toush_links.get(short_string=short_string).toush_link.delete()
                # user.toush_link.get(short_string__exact=short_string).delete()
                # ToushLink.objects.get(short_url__exact=short_string).delete()
            elif typeof == 'account' and identifier and service in url_c_list.values():
                # user.accounts.get(identifier=identifier, service=service).delete()
                user.accounts.filter(service=service).delete()
            else:
                erl.append('IntegrityError')
            
            if len(erl) > 0:
                return DeleteToush(success=False, errors=erl)

            return DeleteToush(success=True)
            

class EditToushLink(graphene.Mutation):
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:

        # link args
        changed = graphene.List(graphene.String, required=True)

        toush_string = graphene.String(required=True)

        accounts_list = graphene.JSONString(required=False)

        custom_link = graphene.String(required=False)
        message = graphene.String(required=False)

        link_to_profile = graphene.Boolean(required=False)
        username = graphene.Boolean(required=False)
        first_name = graphene.Boolean(required=False)
        last_name = graphene.Boolean(required=False)
        contact_phone = graphene.Boolean(required=False)
        #banner =
        contact_email = graphene.Boolean(required=False)
        

    def mutate(self, info, toush_string, changed, accounts_list='', custom_link='', message='', link_to_profile=False, username=False, first_name=False, last_name=False, contact_email=False, contact_phone=False):
        erl = []
        if info.context.user.is_authenticated:
            user = info.context.user
            # put all in try catch lol

            ### TEST THE SPEED
            try:
                link = user.toush_links.get(toush_string=toush_string).toush_link
                item = user.toush_links.get(toush_string=toush_string)
            except: # don't let it execute rest of code so just return here
                erl.append('IntegrityError')
                return EditToushLink(success=False, errors=erl)

            if custom_link and 'custom_link' in changed:
                link.short_url = custom_link
                item.toush_string = custom_link

            if message and 'message' in changed:
                item.message = message
            
            #######

            if not (accounts_list == "{}"):
                print(accounts_list)
                try:
                    # json_accounts_list = json.loads(accounts_list)
                    # print(type(accounts_list), accounts_list["services"])
                    if len(accounts_list["services"]) > 0:
                        item.accounts_list = accounts_list
                except:
                    erl.append('JSONError')
            else:
                erl.append('JSONFormatError')

            #######

            if type(link_to_profile) is bool and 'link_to_profile' in changed:
                item.link_to_profile = link_to_profile

            if type(username) is bool and 'username' in changed:
                item.username = username

            if type(first_name) is bool and 'first_name' in changed:
                item.first_name = first_name

            if type(last_name) is bool and 'last_name' in changed:
                item.last_name = last_name

            if type(contact_email) is bool and 'contact_email' in changed:
                item.contact_email = contact_email

            if type(contact_phone) is bool and 'contact_phone' in changed:
                item.contact_phone = contact_phone

            try:
                link.save()
                item.save()
            except:
                erl.append('IntegrityError')

            if len(erl) > 0:
                return EditToushLink(success=False, errors=erl)

            return EditToushLink(success=True)
            