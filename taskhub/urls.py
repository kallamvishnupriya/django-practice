from django.urls import path
from taskhub.views import dashboard,user_login,signup,tasks,task_create,task_edit,task_delete

urlpatterns=[
    path('dashboard/',dashboard,name='dashboard'),
    path('signup/',signup,name='signup'),
    path('login/',user_login,name='login'),
    path('tasks/',tasks,name='tasks'),
    path('tasks/create/', task_create, name='task_create'),
    path('tasks/edit/<int:id>/',task_edit, name='task_edit'),
    path('tasks/delete/<int:id>/', task_delete, name='task_delete'),
]