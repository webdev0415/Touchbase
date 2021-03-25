import graphene
from apps.tcss.models import TCSS
from apps.cliques.models import Clique
from apps.users.models import User
from apps.users.obj_types import UserType
from apps.cliques.obj_types import CliqueType
from apps.tcss.obj_types import TCSSType

class BrandType(graphene.ObjectType):
    name = graphene.String(default_value='Hioz LLC')
    caption = graphene.String(default_value='We like memes!')

class ExploreLists(graphene.ObjectType):
    people = graphene.List(UserType)
    cliques = graphene.List(CliqueType)
    brands = graphene.List(BrandType)

class Query(object):
    wtf = graphene.List(UserType, count=graphene.Int(), skip=graphene.Int(), default=graphene.Boolean())
    explore = graphene.Field(ExploreLists, page=graphene.Int())
    trending = graphene.List(UserType, count=graphene.Int(), skip=graphene.Int())

    @staticmethod
    def resolve_trending(cls, info, count=None, skip=0, **kwargs):
        if info.context.user.is_authenticated:
            # NOTE: get 35% users who don't often appear on trending, and rest are top of top
            print(skip, count)
            return User.objects.raw('SELECT u.id FROM users_user AS u JOIN users_usersettings AS s on s.user_id = u.id WHERE u.id NOT IN (SELECT followee_id FROM follows_follow WHERE follower_id = %s) AND u.id != %s ORDER BY s.tri_count DESC LIMIT %s OFFSET %s', [info.context.user.id, info.context.user.id, count, skip])
            # return User.objects.raw('SELECT u.id FROM users_user AS u JOIN users_usersettings AS s on s.user_id = u.id WHERE u.id NOT IN (SELECT followee_id FROM follows_follow WHERE follower_id = %s) AND u.id != %s ORDER BY s.tri_count DESC LIMIT 20 OFFSET 20', [info.context.user.id, info.context.user.id])

            return people

    @staticmethod
    # IMPORTANT NOTE: cls = self... the model itself. Change for whole app and use it to optimize
    def resolve_wtf(cls, info, count=None, skip=0, default=False, **kwargs):
        if info.context.user.is_authenticated:
            # NOTE: upgrade to relay nodes later, so no need to refetch form db on fetchmore
            if default:
                # NOTE: MAKE SURE NOT ALREADY FOLLOWING AND HASN'T ALREADY BEEN SEEN IN WTF!
                return User.objects.raw('SELECT u.id FROM users_user AS u JOIN users_usersettings AS s on s.user_id = u.id WHERE has_tcss = True AND u.id NOT IN (SELECT followee_id FROM follows_follow WHERE follower_id = %s) AND u.id != %s ORDER BY s.tri_count DESC LIMIT %s OFFSET %s', [info.context.user.id, info.context.user.id, count, skip])
            else:
                users = User.objects.raw('SELECT id, user_id FROM tcss_tcss_wtf WHERE tcss_id = %s ORDER BY id ASC', [info.context.user.tcss.id])
                if skip:
                    users = users[skip:]
                if count:
                    users = users[:count]
                return users
            

    @staticmethod
    def resolve_explore(cls, info, page=0, **kwargs):
        if info.context.user.is_authenticated:
            people = []
            cliques = []
            brands = [BrandType() for x in range(10)]

            # first page, get first 40 and first 20
            if page == 0:
                for u in TCSS.objects.raw('SELECT id, user_id FROM tcss_tcss_exp_people WHERE tcss_id = %s ORDER BY id ASC LIMIT 45', [info.context.user.tcss.id]):
                    people.append(u.user)
                for c in TCSS.objects.raw('SELECT id, clique_id FROM tcss_tcss_exp_cliques WHERE tcss_id = %s ORDER BY id ASC LIMIT 20', [info.context.user.tcss.id]):
                    cliques.append(Clique.objects.get(id=c.clique_id))
            # second page, skip first 40 and first 20
            elif page == 1:
                # print('page1')
                # NOTE: actual code
                for u in TCSS.objects.raw('SELECT id, user_id FROM tcss_tcss_exp_people WHERE tcss_id = %s ORDER BY id ASC OFFSET 40', [info.context.user.tcss.id]):
                    people.append(u.user)
                for c in TCSS.objects.raw('SELECT id, clique_id FROM tcss_tcss_exp_cliques WHERE tcss_id = %s ORDER BY id ASC OFFSET 20', [info.context.user.tcss.id]):
                    cliques.append(Clique.objects.get(id=c.clique_id))

                # NOTE: test code, remove for prod
                # for u in TCSS.objects.raw('SELECT id, user_id FROM tcss_tcss_exp_people WHERE tcss_id = %s ORDER BY id ASC LIMIT 45', [info.context.user.tcss.id]):
                #     people.append(u.user)
                # for c in TCSS.objects.raw('SELECT id, clique_id FROM tcss_tcss_exp_cliques WHERE tcss_id = %s ORDER BY id ASC LIMIT 20', [info.context.user.tcss.id]):
                #     cliques.append(Clique.objects.get(id=c.clique_id))

            # switch to defaults
            elif page > 1:
                # get default stuffs
                # return that
                defaults_page = page - 1
                pass    

            return ExploreLists(people, cliques, brands)
