from django.urls import path
from .view import RegisterUserView



urlpatterns=[
    path('register', RegisterUserView.as_view(), name='register')
]