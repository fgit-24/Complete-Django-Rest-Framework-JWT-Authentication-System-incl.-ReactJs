from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import send_code_to_user
from .models import OneTimePassword

class RegisterView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        user.data = request.data
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data = serializer.data
            send_code_to_user(user['email'])
            return Response({
                'data': user,
                'message': 'Thanks for signing up! A passcode has been sent to verify your email.'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUserEmail(GenericAPIView):
    def post(self, request):
        otp_code = request.data.get('otp')
        
        if not otp_code:
            return Response({'message': 'OTP code not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_code_obj = OneTimePassword.objects.get(otp_code=otp_code)
            user = user_code_obj.user
            
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({
                    'message': 'Account email verified successfully'
                }, status=status.HTTP_200_OK)
            
            return Response({
                'message': 'User already verified!'
            }, status=status.HTTP_400_BAD_REQUEST)

        except OneTimePassword.DoesNotExist:
            return Response({
                'message': 'Invalid OTP code.'
            }, status=status.HTTP_400_BAD_REQUEST)