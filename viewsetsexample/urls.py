from django.urls import path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from . views import UserViewSet

router=DefaultRouter()
router.register('users',UserViewSet)
urlpatterns=router.urls