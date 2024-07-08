#If we dont use this file, everytime a new user profile is created, we'll have to manually create a profile in the database to contain phone number and address.
#With this file everytime a new user is created, it automatically created a profile for that username



from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()