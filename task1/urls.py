from django.urls import path
from . import views

urlpatterns = [
    path('task1/', views.task1, name='task1'),
    path('delete_task1/<int:id>/',views.delete_task1,name='delete_task1'),
    path('edit/<int:id>/', views.edit_task, name='edit_task')
]