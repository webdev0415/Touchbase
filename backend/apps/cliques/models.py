from uuid import uuid4
from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.users.models import get_it_default, IT_CHOICES
from django.contrib.postgres.fields import ArrayField
# from django.utils.functional import lazy


# def get_cliques_choices():
#     cliques = Clique.objects.all().values_list('name', flat=True)
#     # turn ['big boi mans', 'small boi mans', 'medium boi mans'] into (('big boi mans', 'big boi mans'), ('small boi mans', 'small boi mans'), ('medium boi mans', 'medium boi mans'))
#     return tuple(zip(tuple(cliques), tuple(cliques))) if len(cliques) > 0 else None

class CliqueManager(models.Manager):
    """ Clique manager for extra methods """

    def add_tri_view_count(self, name):
        """ Add 1 view to tri count """
        clique = Clique.objects,get(name=name)
        clique.tri_count += 1
        clique.view_count += 1
        clique.save()

    def create_clique(self, user, name, file, caption):
        """ Create clique """
        clique = user.cliques.create(
            founder = user,
            name = name,
            caption = caption
        )
        file_name = str(clique.token)
        file_format, img_str = file.split(';base64,')
        file_ext = file_format.split('/')[-1] 
        file = default_storage.save(f'{file_name}.{file_ext}', ContentFile(base64.b64decode(img_str)))
        clique.thumbnail = f'https://{settings.AWS_STORAGE_BUCKET_NAME}.{settings.AWS_S3_REGION_NAME}.cdn.digitaloceanspaces.com/{settings.MEDIAFILES_LOCATION}/{clique.token}.jpeg'
        clique.save()
        # clique = Clique()
        # clique.name = name
        # clique.caption = caption
        # clique.thumbnail = thumbnail
        # clique.save()
        # # this is the founder
        # clique.members.add(user.id)

    def join_clique(self, user, name):
        """ Join clique """
        clique = Clique.objects.get(name=name)
        user.cliques.add(clique.id)

    def leave_clique(self, user, name):
        """ Leave clique """
        clique = Clique.objects.get(name=name)
        user.cliques.remove(clique.id)

    # can do clique version history here
    def update_clique(self, user, name, file, caption):
        """ Update clique """
        clique = Cliques.objects.get(name=name)

        if user is clique.founder:
            if name:
                clique.name = name
            if caption:
                clique.caption = caption
            if file:
                file_name = str(clique.token)
                file_format, img_str = file.split(';base64,')
                file_ext = file_format.split('/')[-1] 
                default_storage.delete(f'{file_name}.{file_ext}')

                clique.token = uuid4()
                
                file_name = str(clique.token)
                file_format, img_str = file.split(';base64,')
                file_ext = file_format.split('/')[-1] 
                file = default_storage.save(f'{file_name}.{file_ext}', ContentFile(base64.b64decode(img_str)))
                clique.thumbnail = f'https://{settings.AWS_STORAGE_BUCKET_NAME}.{settings.AWS_S3_REGION_NAME}.cdn.digitaloceanspaces.com/{settings.MEDIAFILES_LOCATION}/{clique.token}.jpeg'
            clique.save()
        else:
            raise Exception('who u tryna fool')


# class UserCliques(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         related_name='cliques',
#         on_delete=models.CASCADE
#     )

#     cliques_list = models.ForeignKey(
#         Clique,
#         related_name='cliques_list',
#         on_delete=models.CASCADE
#     )

    # cliques_list = ArrayField(models.CharField(max_length=32, default='', blank=True), default=get_it_default)


    # def __init__(self, *args, **kwargs):
    #     super(UserCliques, self).__init__(*args, **kwargs)
    #     # check if we need to change the charfield of cliques_list instead
    #     self._meta.get_field('cliques_list').choices = lazy(get_cliques_choices, list)()


class Clique(models.Model):
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='cliques',
    )
    founder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='founded_cliques',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, default='')
    caption = models.CharField(max_length=100, default='')
    thumbnail = models.URLField(max_length=200, default='https://tbdev.nyc3.cdn.digitaloceanspaces.com/m/blank-face.png', verbose_name='profile_pic')
    token = models.UUIDField(verbose_name='Token', default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=timezone.now)

    clique_tags = ArrayField(models.CharField(max_length=32, default='', blank=True, choices=IT_CHOICES), default=get_it_default)

    # trr = trending reset, tri = trending interval, tra = trending appearance
    view_count = models.IntegerField(default=0)
    tri_count = models.IntegerField(default=0)
    tra_count = models.IntegerField(default=0)

    objects = CliqueManager()

    def __str__(self):
        return "%s has %s members" % (self.name, self.members.count())

