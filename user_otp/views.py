from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from rest_framework.response import Response
from .models import CustomerUser
from rest_framework import status
from .Template import *
from Api.models import User
from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from django.conf.urls import include, url
from django.conf import settings


# Create your views here.
@api_view(['POST'])
def reset_request(request):
    data = request.data
    email = data['email']
    user = CustomerUser.objects.get(email=email)
    if CustomerUser.objects.filter(email=email).exists():
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
    
def otp(request):
    return render(request, 'otp.html')




import uuid 
from django.conf import settings
#forgot password method.
def forgot_password(request):
    try:
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            new_email = User.objects.get(email=email)
            def send_forgot_password(email):
                token = str(uuid.uuid4())
                subject = 'Forgot your password link'
                message = f'Click on the link to reset your password{token}'
                email_from = settings.EMAIL_HOST_USER
                recipient = [email]
                send_mail(subject, message, email_from, recipient)
                return True
    except Exception as e:
        print (e)

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_user = User.objects.filter(Q(email=data))
            print(associated_user)
            if associated_user.exists():
                # print(associated_user)
                value = settings.ALLOWED_HOSTS[1]
                print(value)
                for user in associated_user:
                    subject = "Password reset Requested"
                    email_template_name = "password_reset_email.txt"
                    context = {
                        "email": user.email,
                        "domain":str(value),
                        "site_name":"Website",
                        "uid":urlsafe_base64_encode(force_bytes(user.pk)),
                        "user":user,
                        'token':default_token_generator.make_token(user),
                        'protocol':'http',
                    }
                    print (context)
                    email = render_to_string(email_template_name, context)
                    try:
                        send_mail(subject, email, 'sharmaeshu54@gmail.com', ['yashraj.sharma@webmobriltechnologies.com'], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid Header Found')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html", context={"password_reset_form": password_reset_form})

@csrf_exempt
def delete_the_user(request, id, *args, **kwargs):
    if request.method == 'DELETE':
        try:
            if id:
                data = request.GET.get('email')
                user=User.objects.get(data=data)
                user.delete()
                return render_to_string('User is Deleted Successfully')
            else:
                return render_to_string('Error in Code')
        except Exception as e:
            print(e)
    else:
        return HttpResponse('User Deleted Successfully')
  