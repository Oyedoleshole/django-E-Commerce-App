from django.urls import path
# from .views import reset_request, otp
from . import views
app_name="user_otp"
urlpatterns = [
    path('give/otp', views.reset_request, name='otp-given'),
    path('otp/reset/', views.otp, name='otp'),
    path('password_reset', views.password_reset_request , name='password_reset'),
    path('user/delete/<int:id>', views.delete_the_user, name='deleting_the_user')
]