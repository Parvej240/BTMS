from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    FARMAR = 'FARMAR'
    AGRICULTURERIST = 'AGRICULTURERIST'
    VATONARIS = 'VATONARIS'
    IS_DOCTOR = 'DOCTOR'
    IS_USER = 'USER'
    USER_TYPE_CHOICES = [
        (IS_DOCTOR, 'Doctor'),
        (IS_USER, 'User'),
    ]
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default=IS_USER)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        null=True, blank=True, default='250x250.png')
    about = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username
