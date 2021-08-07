from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .managers import AccountManager

class Account(AbstractBaseUser):
    username            =   models.CharField(max_length=255, unique=True)
    email               =   models.EmailField(unique=True)
    date_joined         =   models.DateTimeField(auto_now_add=True)
    last_login          =   models.DateTimeField(auto_now=True)
    is_active           =   models.BooleanField(default=True)
    is_admin            =   models.BooleanField(default=False)
    is_staff            =   models.BooleanField(default=False)
    is_superuser        =   models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.username


