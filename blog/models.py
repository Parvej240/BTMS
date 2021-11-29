from django.db import models
from account.models import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    image = models.ImageField(upload_to='blog', default='720x400.png')
    post_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(
        User, related_name='blog', on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, related_name='likes', blank=True)
    like_count = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
