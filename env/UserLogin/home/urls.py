from django.urls import path
from .views import *



urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('profile',UserDetails.as_view(),name='profile'),
]