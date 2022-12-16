from django.urls import path
from .views import post_the_user_data

urlpatterns = [
    path('user/login/otp/', post_the_user_data, name='creating_the_user_profile'),
]