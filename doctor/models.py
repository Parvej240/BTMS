from account.models import Profile, User
from django.db import models
from django.db.models.fields import CharField
from datetime import date

# Create your models here.


class Booking(models.Model):
    booker = models.ForeignKey(
        Profile, related_name='booking', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    problem = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    fisheries = models.ForeignKey(
        User, related_name='booking', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        return self.problem


class Report(models.Model):
    user = models.ForeignKey(
        User, related_name='report', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    doctor = models.ForeignKey(
        User, related_name='doctor', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.question
