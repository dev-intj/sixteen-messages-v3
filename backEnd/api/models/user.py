from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=28,unique=True)
    email = models.EmailField(unique=True, max_length=64, db_index=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DecimalField(auto_now=True)
    # required from abstract user
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.full_name