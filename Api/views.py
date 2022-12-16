from django.shortcuts import render, HttpResponse, redirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserLoginSerializer, RegisterSerializer, DetailSerializer, UserModelSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib import auth, messages
from Api.models import User, UserModel
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from image.image_models import UploadImages
from rest_framework.decorators import parser_classes
from django.contrib.auth import login as auth_login


class UserDetailApi(APIView,):
    #
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication,]
    #
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        Serializer = UserSerializer(user,)
        return Response(Serializer.data, status=status.HTTP_200_OK)

import json
class RegisterUserAPIView(generics.CreateAPIView,):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


#The accurate fuctionality of register User model;
def user_creation_form(request, **extra_fields):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        if password != confirm_password:
            return render(request, 'error.html',{'error':'Password did not match'})
        elif User.objects.filter(email=email).exists():
            return render(request, 'error.html',{'error': 'Email Already Exists'})
        elif User.objects.filter(firstname= " "):
            messages.info(request, 'Firstname is not blank')
        elif User.objects.filter(lastname= " "):
            messages.info(request, "Lastname is not blank")
        else:
            user=User.objects.create_user(email=email, password=password, first_name=firstname, last_name=lastname)
            user.save()
            return render(request, 'index.html')
    return render(request, 'signup.html')
#End Here.


class UserLoginView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication,]
    serializer_class = UserLoginSerializer
    def get(self, request, format=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email, password=password)
            if user is not None:
                return Response({'msg':'Login Success'}
                )
            else:
                return Response({'msg':'Either Email or Password Would Wrong or else user do not exist in database'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailApi(APIView):
    permission_classes = (AllowAny,)
    serializer_class = DetailSerializer
    def get(self, request, format=None):
        try:
            data = User.objects.all()
            serializer=DetailSerializer(data, many=True)
            return Response({'userdata':serializer.data}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class get_user_detail(APIView):
    permission_classes  = (AllowAny,)
    serializer_class = DetailSerializer
    def get(self, request, id):
        try:
            data=User.objects.get(id=id)
            serializer=DetailSerializer(data)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(serializer.errors)
#Delete the user Data.
class delete_user_details(APIView):
    permission_classes = (AllowAny,)
    def delete(self, request, id=None, format=None):
        user = User.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Update the User Data.
class update_user_details(APIView):
    permission_classes = (AllowAny,)
    def put(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer=DetailSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User details updated.'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#Create the api the user upload his/her name, Photograph and Address.
# def home(request):
#     if request.method=='POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Taken')
#                 return redirect('/index')
#             elif User.objects.filter(first_name=first_name).exists():
#                 messages.info(request, 'First Name already be there')
#                 return redirect('/index')
#             else:
#                 user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
#                 user.save()
#                 return render(request, 'success.html')
#                 print(user)
#     return render(request, 'index.html')


class HomeApiView(RegisterSerializer, APIView,):
    def post(request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            if password != password2:
                return Response({'Password':'Does not match'})
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
            elif User.objects.filter(first_name=first_name).exists():
                messages.info(request, 'First Name already Taken')
            elif User.objects.filter(last_name=last_name).exists():
                messages.info(request, 'Last Name already Taken')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password2)
                user.save()
                return user
                
# The Correct Way to Login the user 
from django.template import context
def user_login(request):
    try:
        if request.method == 'POST':
            email= request.POST.get('email')
            password= request.POST.get('password')
            new_user=authenticate(email=email, password=password)
            name = request.session['User_name'] = new_user.first_name
            context = {'username':name}
            print(new_user)
            print(context)
            if new_user is None:
                url = reverse_lazy('login')
                messages.info(request, 'Either Email or Password Would be Wrong')
                return redirect(request, 'login')
            else:
                
                auth_login(request, new_user)
                return render(request, 'dashboard.html', {'context':context})
                return HttpResponse(new_user)
        else:
            return render(request, 'login.html')

    except Exception as e:
        messages.info(request, 'Something is wrong')
        return render(request,'login.html')
        print(e)
#Login End Here.


from .serializer import MessageSerializer, MessageModel
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        new_user = MessageModel(email=email, subject=subject, name=name, phone=phone, message=message)
        if MessageModel.objects.filter(email=email).exists():
            messages.info(request, 'User already exists')
        else:
            new_user.save()
    return render(request, 'contact.html')
    # else:
    #     messages.info(request, 'Details already have been there')
           

def about(request):
    data = User.objects.all()
    context = {'data': data}
    print(context)
    return render(request, 'about.html', context)

def homepage(request):
    return render(request,'homepage.html')

def home(request):
    all_user=UploadImages.objects.all()
    data = {'all_user':all_user,}
    print(data)
    return render(request, 'index.html', data)

def services(request):
    return render(request, 'services.html')

#Delete the User Account from HTML template
class delete_user(SuccessMessageMixin, generic.DeleteView):
    model = User
    template_name = 'delete_user_confirm.html'
    success_message = 'User has been deleted successfully'
    success_url = reverse_lazy('index.html')


class user_delete(APIView):
    model = User
    def delete(self, request, id):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            model(email=email, password=password)
            if model.objects.filter(email=email).exists():
                model.delete()
                return render (request, 'index.html')
            else:
                messages.info(request, 'User is not been found')
        else:
            return reverse_lazy('homepage.html')


# def UserDeleteInformation(request, pk):
#     if request.method == 'DELETE':


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        new_user = authenticate(email=email, password=password)
        messages.info(request, 'Signed In with')
        return redirect(request, 'signup.html')
    else:
        messages.info(request, 'Email or Password would be wrong')
        return render(request, 'error.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['confirm_password']
        new_user = User(email=email, first_name=firstname, last_name=lastname)
        if password != password2:
            messages.info(request, 'Password do not match')
            return render(request, 'error.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'User already exists')
            return render(request, 'error.html')
        else:
            new_user.save()
            return render(request, 'login.html')
    else:
        return render(request, 'signup.html')

#         if password != password2 and User.objects.filter(email=email).exists():
#             return render(request, 'error.html')
#         else:
#             new_user.save()
#     return render(request, 'signup.html')

def error(request):
    return render(request,'error.html')

from django.db import transaction

@transaction.non_atomic_requests
def my_view(request):
    return do_stuff

@transaction.non_atomic_requests(using='other')
def my_other_view(request):
    return do_stuff_on_the_other_database


from django.http import JsonResponse
@api_view(['POST'])
@authentication_classes([JWTAuthentication,])
@parser_classes([JSONParser, MultiPartParser, FormParser])

def post_user_create(request):
    email=request.GET.get('email')
    password=request.GET.get('password')
    password2=request.GET.get('password2')
    first_name=request.GET.get('first_name')
    last_name=request.GET.get('last_name')
    if password != password2:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    elif User.objects.filter(email=email).exists():
        return Response('User in this email is already registered')
    else:
        user=User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        data={"email":user.email,
        "first_name":first_name,
        "last_name":last_name}
        json.dumps(data)
        user.save()
        return JsonResponse(data, status=status.HTTP_201_CREATED)


def map(request):
    data = list(Map.objects.values('lat', 'lng', 'description'))
    return render(request, "map.html", {'data': data})


#Tomorrow task are make a PUT, PATCH and DELETE API's ?
#User Delete and Update his/her details.

class user_update_details(APIView):
    permission_classes = [AllowAny]
    authentication_classes  = [JWTAuthentication,]
    serializer_class = [UserModelSerializer]
    def get(self, request):
        data=UserModel.objects.all()
        serializer=UserModelSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = UserModelSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

from rest_framework import mixins
class GenericAPIView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,):
    lookup_field = 'id'
    serializer_class=UserModelSerializer
    queryset=UserModel.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    queryset=UserModel.objects.all()

    def get_queryset(self):
        return UserModel.objects.all(id=self.request.user.id)

    def put(self, request, id):
        return self.update(request, id)
  

    def delete(self, request, id):
        return self.destroy(request, id)
        
    def get(self, request):
        return self.retrieve(request)

@api_view(['POST'])
@permission_classes([AllowAny,])
@authentication_classes([JWTAuthentication])
def get_user_token(request):
    try:
        data=JsonParser().parse(request)
        serializer = UserLoginSerializer(data)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        print(email, password)
        user = authenticate(email=email, password=password)
        token = Token.objects.get_or_create(user=user)[0]
        if user is not None:
            return Response({'token':token})
        return Response({'token':None})
    except Exception as e:
        print(e)
        return Response({'error':e})

from django.urls import reverse, reverse_lazy
import os
from twilio.rest import Client
import random

def article(request):
    url1 = reverse('index')
    url2 = reverse_lazy("homepage")
    print(type(url1))
    print(type(url2))
    return HttpResponse("URL1=%s , URL2=%s" % (url1, url2))
    account_sid = 'ACc829b3fdb3823ad0f4ee572a75f02b28'
    auth_token = 'f2a9c0985281be9ff528d2ed8e4ca036'
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body=("This message is sent from Django Admin" ,random.randint(1000,9999)),
                     from_='+14095097862',
                     to='+9105129554864869'
                 )
    print(message.sid)
    return redirect(url1)

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        if user.email.exists():
            password=password.save()
        else:
            return messages.info(request, 'Password do not match'),
            reverse_lazy('index')
    else:
            messages.info(request, 'Password do not match')
    return render(request, 'forgot_password.html')

from django.contrib.auth.views import PasswordChangeForm, PasswordChangeView
class PasswordsChangeView(PasswordChangeView):
    from_class = forgot_password
    success_url = reverse_lazy('index')


###############################################################################
# Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client



# account_sid = os.environ['ACc829b3fdb3823ad0f4ee572a75f02b28']
# auth_token = os.environ['f2a9c0985281be9ff528d2ed8e4ca036']
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="This message is sent from Django Admin",
#                      from_='+14095097862',
#                      to='+917838727194'
#                  )

# print(message.sid)
