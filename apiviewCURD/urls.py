from django.urls import path
from django.contrib import admin
from .views import ItemList

urlpatterns=[
    path('admin/',admin.site.urls),
    path('get/',ItemList.as_view())
]