from django.db.models.signals import post_save
from .models import User, Profile


def user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile Created.")


post_save.connect(user_profile, sender=User)
