# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

#Create CustomUserManager
class CustomUserManager(BaseUserManager,):
    use_in_migrations = True
    def _create_user(self, email, password, first_name, last_name, mobile, **extra_fields,):
        if not email:
            raise ValueError('Email Must Be Provided')
        if not password:
            raise ValueError('Password is not Provided')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def __create_user(self, email, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError('Please Provide Email')
        if not password:
            raise ValueError('Please Provide Password')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user    

    def create_user(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self.__create_user(email, password, first_name, last_name, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin,):
    #AbstractBaseUser has only three fields{Password, Last_login, Is_active}
    email=models.EmailField(unique=True, max_length=100)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    mobile=models.CharField(max_length=50, default='000000000')
    address=models.CharField(max_length=200)
   
    is_staff=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    objects=CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','mobile']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
#for Image upload. 


class UserModel(models.Model):
    email=models.EmailField(unique=True, max_length=100)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    id=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.first_name

# class PaymentModel(models.Model):
#     name=models.CharField(max_length=100)
#     amount=models.IntegerField(
#         def validate(self, attrs):
#             if attrs['amount']<=0:
#                 raise ValidationError('amount must be greater than zero')
#             return attrs
#     )
#     discription=models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class PaymentModelSerializer(serializers.ModelSerializer):
#     email=serializer.EmailField(max_length=20)
#     class Meta:
#         model=PaymentModel
#         fields = ['name', 'amount', 'description']