
from django.db.models import query



from .serializers import *
from django.contrib.auth import login
from .models import *


from rest_framework import viewsets

from rest_framework import filters



# from django.contrib.auth.models import User


class ContactViewSet(viewsets.ModelViewSet):
    search_fields=['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer  