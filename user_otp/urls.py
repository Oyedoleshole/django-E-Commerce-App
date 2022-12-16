from django.urls import path
from .views import reset_request
urlpatterns = [
    path('give/otp', reset_request, name='otp-given')
]