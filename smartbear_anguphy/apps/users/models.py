from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField('First name', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Last name', max_length = 255, blank = True, null = True)
    email = models.EmailField('Email', max_length = 255, unique = True)
    password = models.CharField('Password', max_length = 100)
    username = None
 
    birthday = models.DateTimeField('Birthday Date', blank = True, null = True)
    address = models.CharField('Address', max_length = 255, blank = True, null = True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
