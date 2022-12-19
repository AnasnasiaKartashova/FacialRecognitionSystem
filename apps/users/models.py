from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="media", null=True, blank=True)
    timekeeping = models.DateTimeField(null=True, blank=True)
