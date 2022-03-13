from argparse import _SubParsersAction


import datetime
datetime.datetime.now()
from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField
from datetime import date, datetime as dt
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class Contact(models.Model):
   
    name = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=60, blank=True)
    subject = models.CharField(max_length=60, blank=True)
    message = models.CharField(max_length=300, blank=True)
    

    def __str__(self):
        return f'{self.user.username}'   