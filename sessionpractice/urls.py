from django.contrib import admin
from django.urls import path, include
from sessionpractice.views import show_enrollements,create_enroll

urlpatterns = [
    path('enroll/<int:sid>/<int:cid>/', create_enroll),
    path('show-enrollments/', show_enrollements),
]