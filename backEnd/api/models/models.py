from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.conf import settings

class Language(models.Model):
    #https://www.science.co.il/language/Codes.php
    english_name = models.CharField(max_length=16)
    code_2 = models.CharField(max_length=2)
    code_3 =models.CharField(max_length=2)

class Account(models.Model):
    email = models.EmailField(max_length = 100,unique=True)
    password = models.CharField(max_length = 24)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    username = models.CharField(max_length = 25,unique=True,blank=False)
    biography = models.CharField(max_length = 250,blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    date_created = models.DateTimeField(auto_now_add=True)
    mbtiType = models.CharField(max_length = 6,blank=True)
    enneagram = models.CharField(max_length = 3,blank=True)
    friends = models.ManyToManyField("Profile", blank=True)
    
    def __str__(self):
        return self.username

class FriendRequest(models.Model):
	to_user = models.ForeignKey(Profile, related_name='to_user', on_delete=models.CASCADE)
	from_user = models.ForeignKey(Profile, related_name='from_user', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "From {}, to {}".format(self.from_user.username, self.to_user.username)

def get_sentinel_user():
    return Profile().objects.get_or_create(username='deleted')[0]

class Message(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.SET(get_sentinel_user)
    )
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    message = models.CharField(max_length = 300)
    language = models.CharField(max_length=3,default="EN")
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Type:{}, message {}".format(self.profile.mbtiType,self.message)