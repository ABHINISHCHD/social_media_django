from distutils.command.upload import upload
from email.policy import default
from importlib.metadata import requires
from pydoc import locate
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from jinja2 import ModuleLoader
# Create your models here.

class follow(models.Model):
    follower=models.CharField(max_length=1000)
    user=models.CharField(max_length=1000)


class like(models.Model):
    post_id=models.CharField(max_length=100)
    username=models.CharField(max_length=100)

    def __str__(self):
        return self.username


class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    bio=models.CharField(max_length=50)
    dp=models.ImageField(upload_to='profile-images',default='profile.png')
    location=models.CharField(max_length=20)
    cover=models.ImageField(upload_to='cover-images',default='cover.jpg')
    

    @property
    def imageurl(self):
        try:
            url=self.dp.url
        except:
            url=''
        return url
    @property
    def coverurl(self):
        try:
            url=self.cover.url
        except:
            url=''
        return url


    def __str__(self):
        return self.name


class posting(models.Model):
    person=models.ForeignKey(profile,on_delete=models.CASCADE)
    post=models.ImageField(upload_to='post',blank=True,null=True)
    likes=models.IntegerField(default=0)
    caption=models.CharField(max_length=50)
    date_post=models.DateField(auto_now_add=True)
    @property
    def imageurl(self):
        try:
            url=self.post.url
        except:
            url=''
        return url

class comment(models.Model):
    post_id=models.CharField(max_length=100)
    comment=models.TextField(max_length=100)
    person=models.ForeignKey(posting,on_delete=models.CASCADE)

    def __str__(self):
        return self.post_id
