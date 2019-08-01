from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Video(models.Model):
    user_id = models.CharField(max_length=30)
    liked_by = models.ManyToManyField(User)

class SearchVideo(models.Model):
    request_string = models.CharField(max_length=30)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)



# from django.db import models
# from django.conf import settings
#
# class Article(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL)
#
#
#
# class User(models.Model):
#     id =
#     username = models.CharField(max_length=30)
#     password = models.IntegerField(max_length=10)
#     likes = models.ManyToManyField(Likes)
#
#
# class Likes(models.Model):
#     id =
#     userid = models.CharField(max_length=30)
#     user = models.ManyToManyField(User)
#
#
# class SearchVideo(models.Model):
#     id =
#     search = models.CharField(max_length=30)
#     relationlikes = models.ForeignKey(Likes, on_delete=models.CASCADE)
#
#
#
#
#
#
# id = models.IntegerField()
# usermane = models.CharField(max_length=30, verbose_name="Enter your nickname")
# password = models.CharField(max_length=30, verbose_name ="Enter your password")
# search =