from django.urls import path
from .views import creating_the_slug_url
urlpatterns = [
    # path('/slug/<str:slug>', myslug ),
    path('create_the_url', creating_the_slug_url, name='create_the_slug_url')
]