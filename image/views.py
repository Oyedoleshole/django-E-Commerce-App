from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from Api.serializer import UserLoginSerializer, RegisterSerializer, DetailSerializer
from rest_framework import status
from Api.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
 #//Create the api takes image,first_name last_name as a argument?
class user_upload_details_view(APIView):
    def save_profile(self):
        try:
            json = self.request.json_body
            #username = str(json['userName'])
            first_name = str(json['firstName'])
            last_name = str(json['lastName'])
            phones = str(json['phones'])
            emails = str(json['emails'])
            self.profiles.update(firstName=first_name, lastName=last_name, emails=emails, phones=phones)
            value = {'result:': 'success', 'message': 'Profile Saved!'}
        except Exception:
            value = {'result': 'error', 'message': 'There was an error processing the request'}

    #returns a json response

class user_auth_jwt(APIView):
    authentication_classes = [JWTAuthentication,]
    permission_classes=(AllowAny,)
    def get(self, request, id, format=None):
           data=User.objects.get(id=id)
           serializer=DetailSerializer(data)
           return Response({'msg':'user is logged in with jwt'})

from .image_serializer import image_upload_serializer
from .image_models import UploadImages
class user_upload_details(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None, id=None):
        serializer = image_upload_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#User Update His address
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def get_all_user_data(request, id):
        if request.method == 'GET':
            data = UploadImages.objects.filter(id=id)
            serializer = image_upload_serializer(data, many=True)
            return JsonResponse (serializer.data, safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse ({'Not data': 'Wrong Inside Code'}, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#This is the generic class based Views.
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
class GenericAPIView(generics.GenericAPIView, mixins.UpdateModelMixin, ):
    serializer_class = image_upload_serializer
    queryset = UploadImages.objects.all()
    lookup_field='id'
    if id:
        def put(self, request, id=None, ):
            return self.update(request)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response({'msg':'Updated Successfully'}, status=status.HTTP_200_OK)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


