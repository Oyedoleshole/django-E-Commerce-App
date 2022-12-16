from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from rest_framework.response import Response
from .models import CustomUser
from rest_framework import status
# Create your views here.
@api_view(['POST'])
def reset_request(request):
    data = request.data
    email = data['email']
    user = CustomUser.objects.get(email=email)
    if CustomUser.objects.filter(email=email).exists():
        # send email with otp
        send_mail(
        'This message is auto generated',
        f'Here is the message with {user.otp}.',
        'sharmaeshu54@gmail.com',
        ['sharmayashraj37@gmail.com'],
        fail_silently=False,
        )
        
        message = {
            'detail': 'Success Message'}
        return Response(message, status=status.HTTP_200_OK)
    else:
        message = {
            'detail': 'Some Error Message'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)