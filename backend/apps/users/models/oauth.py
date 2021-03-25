from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField, ArrayField
from django.conf import settings

def get_pdj_default():
    ### 
    return [
        {'some_post_data': stuff, 'some_post_data': stuff},
        {'some_post_data1': stuff, 'some_post_data4': stuff},
        {'some_post_data2': stuff, 'some_post_data5': stuff},
    ]

def get_spfl_default():
    return []

class OAuthPost(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='OAuthPosts',
        on_delete=models.CASCADE
    )

    created = models.DateTimeField(verbose_name='Created at', auto_now_add=timezone.now)
    service = models.CharField(max_length=100, default='')

    pdj = JSONField(default=get_pdj_default)

    

    def __str__(self):
        # return f"{self.user} -- {self.service}"
        return str(self.user)


# class GlobalSPFLID(models.Model):
#     spfl_id = JSONField(default=get_spfl_default)

class GlobalSPFLID(models.Model):
    spfl_id = ArrayField(models.IntegerField())


class SPFServiceID(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    youtube = models.CharField(max_length=200, default='', null=True)
    steam = models.CharField(max_length=200, default='', null=True)
    soundcloud = models.CharField(max_length=200, default='', null=True)
    reddit = models.CharField(max_length=200, default='', null=True)
    pinterest = models.CharField(max_length=200, default='', null=True)