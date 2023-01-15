from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Fields
    photo = models.ImageField(upload_to="media", null=True, blank=True)
    timekeeping = models.DateTimeField(null=True, blank=True)
    first_name = models.CharField(max_length=200, verbose_name="User Fires Name", null=True, blank=True)
    last_name = models.CharField(max_length=200, verbose_name="User Last Name", null=True, blank=True)
    face_encoding = models.ForeignKey('Encoding',  on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.username


class Encoding(models.Model):
    user_encoding = models.CharField(max_length=2000, verbose_name="User face encoding", null=True, blank=True)

    def __str__(self):
        return self.user_encoding



