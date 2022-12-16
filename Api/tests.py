from django.test import TestCase
from image.image_models import UploadImages
# Create your tests here.

class UploadImageTestCase(TestCase):
    def setUp(self):
        UploadImages.objects.create(first_name='Yashraj')
        UploadImages.objects.create(last_name='Sharma')
        UploadImages.objects.create(address='45/69, Shastri Nagar')

    def UploadImagesTest(self):
        obj1=UploadImages.objects.get(first_name='Yashraj')
        obj2=UploadImages.objects.get(last_name='Sharma')
        obj3=UploadImages.objects.get(address='45/69, Shastri Nagar')
        self.assertEqual(obj1.first_name, 'Yashraj')
        self.assertEqual(obj2.last_name, 'Sharma')
        self.assertEqual(obj3.address, '45/69, Shastri Nagar')


