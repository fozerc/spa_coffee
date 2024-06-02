from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class SpaUser(AbstractUser):
    avatar = models.ImageField(blank=True, null=True)
