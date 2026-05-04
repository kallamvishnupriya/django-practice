from django.urls import path
from contact.views import contact_view, success_view

urlpatterns = [
     path('contact_form/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]