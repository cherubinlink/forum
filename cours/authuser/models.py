from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=500, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    localisation = models.CharField(max_length=100,null=True)
    avatar = models.ImageField(upload_to='media/avataruser', null=True,blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
