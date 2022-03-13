from django.urls.conf import path,include
from . import views

from django.urls import path
from knox import views as knox_views

from django.urls import path
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *  
from rest_framework_jwt.views import obtain_jwt_token 



router = DefaultRouter()
 

router.register('contact',ContactViewSet,basename='contact')

urlpatterns=[
     path('',include(router.urls)),
    

] 
