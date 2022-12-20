"""django_settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_otp import views
#These Things were added by me.
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  
from Api.views import homepage
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listapi/', include('Api.urls')),
    path('image/', include('image.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/', include('image.urls')),
    path('data/', include('image.urls')),
    path('generic/', include('image.urls')),
    path('', homepage, name='homepage'),
    path('generate-otp/', include('user_login_with_otp.urls'), name='user-login-with-otp-file'),
    path('phone/', include('user_otp.urls')),
    path('slug', include('uses_of_slug_field.urls')),
    #Changing Password Functionality.
    # path('accounts/', include('django.contrib.auth.urls'))
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('reset/<str:uidb64>/<str:token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset', views.password_reset_request , name='password_reset'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    # ... the rest of your URLconf goes here ...
    

    



