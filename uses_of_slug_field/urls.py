from django.urls import path
from .views import myslug
urlpatterns = [
    path('/slug/<str:slug>', myslug )
]