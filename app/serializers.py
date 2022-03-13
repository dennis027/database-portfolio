from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models, transaction
from .models import *
from cloudinary.models import CloudinaryField

from django.contrib.auth import get_user_model
from django.db import models, transaction
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import filters

from rest_framework import serializers
from django.contrib.auth.models import User


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name','email','subject','message')