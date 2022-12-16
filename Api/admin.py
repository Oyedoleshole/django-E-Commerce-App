from django.contrib import admin
from Api.models import User, UserModel

# Register your models here.
admin.site.register(User)
admin.site.register(UserModel)

from image.image_models import UploadImages
admin.site.register(UploadImages)

from Api.views import MessageModel
admin.site.register(MessageModel)

from user_login_with_otp.models import Profile
admin.site.register(Profile)

from uses_of_slug_field.models import Article
admin.site.register(Article)



