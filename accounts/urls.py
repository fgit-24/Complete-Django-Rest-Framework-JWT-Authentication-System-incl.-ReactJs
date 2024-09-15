from django.urls import path
from .views import RegisterView, VerifyUserEmail



urlpatterns=[
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyUserEmail.as_view(), name='verify'),
]