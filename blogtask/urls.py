from django.urls import path
from django.contrib import admin
from . views import post,home,delete,read,edit,back

urlpatterns=[
    path('admin/',admin.site.urls),
    path('post/',post,name='post'),
    path('home/',home,name='home'),
    path('delete/<int:id>/',delete,name='delete'),
    path('read/<int:id>/',read,name='read'),
    path('edit/<int:id>/',edit,name='edit'),
    path('back/',back,name='back')
]