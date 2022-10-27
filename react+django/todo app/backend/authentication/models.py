from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fav_color = models.CharField(blank=True, max_length=120)
