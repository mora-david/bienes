from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CustomUSer(Base, AbstractBaseUser):
    usuario = models.CharField(
        ('usuario'),
        max_length=150,
        unique=True,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    nombre = models.CharField(max_length=180)

    USERNAME_FIELD = 'usuario'

    objects = UserManager()

class Bienes(Base):
    articulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    usuario_id = models.ForeignKey(CustomUSer, on_delete=models.CASCADE)

    