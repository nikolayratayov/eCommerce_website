from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', register, name='login'),
    path('logout/', register, name='logout'),
]
