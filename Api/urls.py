from django.urls import path
from .views import UserDetailApi, RegisterUserAPIView, UserLoginView, get_user_detail, delete_user_details, update_user_details, home, HomeApiView, user_login, homepage, about, services
from Api.views import contact, delete_user, post_user_create, login, signup, error, user_creation_form, user_update_details, GenericAPIView, get_user_token, article
from . import views
urlpatterns = [
    path('getdetails', UserDetailApi.as_view()),
    #register the User
    path('register', post_user_create, name='checking the query api'),
    #Login the User.
    path('login', UserLoginView.as_view(), name='login_functionalty_is_not_working'),
    #individual User
    path('user/<int:id>',get_user_detail.as_view(), name='Individual User Details'),
    #Delete the User Details
    path('remove/<int:id>',delete_user.as_view(), name='Delete the user'),
    #Update the User Data.
    path('update/<int:pk>', update_user_details.as_view(), name='Update the Data'),
    #Render the HTML page.
    path('index', home, name='index'),
    #Render the Login Page.
    path('signin', user_login, name='user_login'),
    #Render the Home Page.
    path('homepage', homepage, name='homepage'),
    #Render the contact page.
    path('contact', contact, name='contact'),
    #Render the about page.
    path('about', about, name='about'),
    #Render the Services page.
    path('services', services, name='services'),
    #Render the Delete HTML page and user has deleted.
    path('delete_user/<int:pk>/', delete_user.as_view(), name='delete_user'),
    #Render the Signin Page.
    path('user/signin', user_login, name='login'),
    #Render the Signup Page.
    path('user/signup', user_creation_form, name='signup'),
    #Render the error Page.
    path('error', error, name='error.html'),
    
    path('user/update/details/<int:id>/', GenericAPIView.as_view(), name="User Update his/her details"),
    path('user/delete/details/<int:id>', GenericAPIView.as_view(), name="User Delete his/her details"),
    path('user/post/details/', user_update_details.as_view(), name="User Delete his/her details"),
    path('user/get/details/', GenericAPIView.as_view(), name="User Delete his/her details"),
    path('user/get/token/', get_user_token, name="token getting"),

    path('article/', article, name="article" ),
    path('forgot-password/', views.PasswordsChangeView.as_view(template_name='forgot_password.html'), name='forgot-password'),
    # user_login_with_otp App.
]

# from Api.views import my_view, my_other_view
# urlpatterns = [
#     path('my_view', my_view, name='transaction'),
#     path('my_other_view', my_other_view, name='other transactions')

# ]