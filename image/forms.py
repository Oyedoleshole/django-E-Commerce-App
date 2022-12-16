from django import forms
from .image_models import UploadImages

class ImageForm(forms.ModelForm):
    class Meta:
        model = UploadImages
        fields = ['first_name', 'last_name', 'address', 'image']