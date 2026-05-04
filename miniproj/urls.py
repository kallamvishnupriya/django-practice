from django.urls import path
from miniproj.views import login,dashboard

urlpatterns=[
    path('minilogin/',login,name='login'),
    path('minidashboard/',dashboard,name='dashboard'),
]