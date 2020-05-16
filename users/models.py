from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, phone, password = None):
        if not username:
            raise ValueError("Must have a username!")
        elif not email:
            raise ValueError("Must have an email!")
        elif not phone:
            raise ValueError("Must have a phone number!")

        user = self.model(
            username = username,
            phone = phone,
            email = email,
        )

        user.set_password(password)
        user.is_active = True
        user.save(using = self._db)
        return user

    def create_superuser(self, username, phone, email, full_name=None, password = None):
        user = self.create_user(
            username = username,
            phone = phone,
            email = email,
            full_name = full_name,
            password = password
        )

        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here
class User(AbstractBaseUser):
    username = models.CharField(max_length = 30, unique=True)
    full_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 45, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password','email','phone']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True