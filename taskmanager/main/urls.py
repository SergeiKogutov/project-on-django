from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='Logout'),
    path('', views.index1, name='Home'),
    path('create', views.create, name='Create')
]
