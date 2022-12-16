from django.urls import path
from image.views import user_upload_details, get_all_user_data, GenericAPIView

urlpatterns=[
    path('upload',user_upload_details.as_view(), name='User upload details'),
    path('alldetail/<int:id>', get_all_user_data, name='all user details'),
    path('improvements/<int:id>', GenericAPIView.as_view(), name='Generic Api View')
]