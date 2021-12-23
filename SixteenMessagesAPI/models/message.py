from django.db import models
import uuid

class Message(models.Model):
    user = models.ForeignKey("SixteenMessagesAPI.Profile", verbose_name=("user"), on_delete=models.CASCADE)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    message = models.TextField(max_length=128,blank=False,null=False)
    can_be_shared = models.BooleanField(default=True)
    show_user = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'messages'
        app_label = 'SixteenMessagesAPI'
    
    def __str__(self):
        return str(self.user)