from re import search
from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from django.contrib.auth import login
from .models import *
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, generics,permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import filters
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

# from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated  
from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

class ContactViewSet(viewsets.ModelViewSet):
    search_fields=['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer  