from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    specializare = models.CharField(blank=True, max_length=120)
    grupa_sanguina = models.CharField(blank=True, max_length = 20)
    job = models.CharField(blank=True, max_length = 20)