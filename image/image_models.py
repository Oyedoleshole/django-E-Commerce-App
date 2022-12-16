from django.db import models
class UploadImages(models.Model):
    first_name = models.CharField(max_length=255, unique=True, default=True)
    last_name = models.CharField(max_length=255, unique=True, default=True)
    address = models.CharField(max_length=255, null=True)
    caption=models.CharField(max_length=200, blank=True)
    image=models.ImageField(max_length=255, upload_to='media/images', null=True, blank=True)
    

    def __str__(self):
        return self.first_name