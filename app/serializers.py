
from rest_framework import serializers

from .models import *
from cloudinary.models import CloudinaryField

from django.db import models, transaction


from rest_framework import serializers
from django.contrib.auth.models import User


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name','email','subject','message')