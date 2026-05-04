from django.urls import path
from .views import one,two

urlpatterns = [
    path('post/',one),
    path('get/<int:id>/',two)
]