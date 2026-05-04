from django.urls import path
from django.contrib import admin
from .views import HelloView

urlpatterns=[
    path('home/',HelloView.as_view()),
    path('home/<int:id>/', HelloView.as_view())
]