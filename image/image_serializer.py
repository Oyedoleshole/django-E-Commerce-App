from rest_framework import serializers
from .image_models import UploadImages
class image_upload_serializer(serializers.ModelSerializer):
    class Meta:
        model= UploadImages
        fields=['first_name', 'last_name', 'address', 'image']