from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ArticleSerializer
from rest_framework import status
# Create your views here.
@api_view(['POST'])
def creating_the_slug_url(request, *args, **kwargs):
    data = request.data
    serializer = ArticleSerializer(data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
        