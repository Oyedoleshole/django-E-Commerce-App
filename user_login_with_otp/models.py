from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class Another_user_method(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, first_name, last_name, mobile, password, **kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_active',True)
        kwargs.setdefault('is_superuser',False)
        return self.make_user(email, first_name, last_name, password, mobile, **kwargs)

    def make_user(self, email, first_name, last_name, mobile, password,  **kwargs):
        if not email:
            raise ValueError('Email Must Be Provided')
        if not mobile:
            raise ValueError('Mobile Number Must Be Provided')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class Profile(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    mobile = models.CharField(max_length=100, default='1234567890')

    is_staff=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    
    objects = Another_user_method()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']
    USERNAME_FIELD  = 'email'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.email