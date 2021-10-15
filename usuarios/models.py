from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import gettext_lazy as _

class BaseUserManagerModificado(BaseUserManager):
    def create_user(self,email,password):
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return  user

    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return  user

class Usuario(AbstractBaseUser, PermissionsMixin):
    usuario = models.CharField(max_length=30, unique=True, null=False)
    email = models.CharField(max_length=60, unique=True, null=False)
    password = models.CharField(_('password'), max_length=120)
    primer_nombre = models.CharField(max_length=30, unique=False, null=False)
    primer_apellido = models.CharField(max_length=30, unique=False, null=False)
    ci = models.CharField(max_length=10, unique=True, null=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)

    objects = BaseUserManagerModificado()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    #REQUIRED_FIELDS = ['usuario']