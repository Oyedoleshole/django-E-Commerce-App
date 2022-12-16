from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
def myslug(request, slug):
    return Response(request, slug)