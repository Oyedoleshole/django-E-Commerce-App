from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from django.views.decorators.csrf import csrf_exempt
import os
from twilio.rest import Client
# Create your views here.
try:
    @csrf_exempt
    def post_the_user_data(request):
        if request.method == 'POST':
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            mobile = request.POST.get('mobile')
            user = Profile.objects.create_user(email=email, first_name=first_name, last_name=last_name, mobile=mobile)
            print(user)
            if Profile.objects.filter(email=email).exists():
                return render(request, 'error.html')
            else:
                user.save()
                return render(request, 'register.html')
                return HttpResponse({'msg':'User created successfully'}, user)
        else:
            return render(request, 'register.html')
            return HttpResponse({'msg':'use the post method to create the user profile'})
except Exception as e:
    print(e)

    
            
