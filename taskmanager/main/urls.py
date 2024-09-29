from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('edit/<int:task_id>/', edit_task, name='Edit'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('task', views.index, name='Home'),
    path('create', views.create, name='Create'),
    path('registr', RegisterUser.as_view(), name='Register'),
    path('', views.LoginUser, name='Login')
]
