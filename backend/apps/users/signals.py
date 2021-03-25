from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User, UserProfile, AccessData, UserSettings
from apps.users.documents import UserDocument

### SIGNALS ###

@receiver(post_save, sender=User)
def create_user_objects(sender, instance, created, **kwargs):
	# NOTE: checking created may cause issue? check to see
	if created:
		UserProfile.objects.create(user=instance)
		UserSettings.objects.create(user=instance)
		AccessData.objects.create(user=instance)
		# instance.indexing()


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.save()

# @receiver(post_save, sender=User)
# def create_accessdata(sender, instance, created, **kwargs):
#     if created:
#         AccessData.objects.create(user=instance)

# post_save.connect(create_profile, sender=User)



# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.user.save()

# @receiver(post_save, sender=User)
# def create_accessdata(sender, instance, created, **kwargs):
#     if created:
#         AccessData.objects.create(user=instance)

# post_save.connect(create_profile, sender=User)