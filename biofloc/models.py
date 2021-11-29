from django.db import models

from account.models import User

# Create your models here.


class Newsletter(models.Model):
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email


class Build_tank(models.Model):
    tanks = models.IntegerField()
    water = models.IntegerField()
    fish = models.IntegerField()
    food = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
