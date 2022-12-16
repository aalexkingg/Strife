from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    word1 = models.CharField(max_length=128, unique=False, blank=False)
    word2 = models.CharField(max_length=128, unique=False, blank=False)
    word3 = models.CharField(max_length=128, unique=False, blank=False)

    login_attempts = models.IntegerField(default=0)

    disabled = models.BooleanField(default=0)

    #first_name = None
    #last_name = None
    #email = None


