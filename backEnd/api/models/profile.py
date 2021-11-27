from django.db import models

def get_profile_image_filepath(self,filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "profile_images/logo_1080_1080.png"

class Profile(models.Model):
    user = models.OneToOneField(
        "api.CustomUser",
        db_index=True,
        on_delete=models.PROTECT,
        related_name="user",
    )
    
    first_name = models.CharField(blank=True,max_length=30)
    last_name = models.CharField(blank=True,max_length=30)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath,null=True,blank=True,default=get_default_profile_image)
    hide_name = models.BooleanField(default=True)
    hide_email = models.BooleanField(default=True)
    
    class Meta:
        app_label="api"
        db_table='profile'
    
    def __str__(self):
        return str(self.user)
    
    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]