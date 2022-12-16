from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
