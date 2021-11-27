from django.db import models


class Profile(models.Model):
    first_name = models.CharField(blank=True,max_length=30)
    last_name = models.CharField(blank=True,max_length=30)
    profile_image = models.ImageField(max_length=255, upload_to=,null=True,blank=True,default=)