from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    timekeeping = models.DateTimeField(null=True, blank=True)
    first_name = models.CharField(max_length=200, verbose_name="User Fires Name", null=True, blank=True)
    last_name = models.CharField(max_length=200, verbose_name="User Last Name", null=True, blank=True)
    face_encoding = models.ForeignKey(
        'UserEncoding',
        on_delete=models.PROTECT,
        related_name="user",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username


class UserEncoding(models.Model):
    photo1 = models.ImageField(null=True, blank=True)
    photo2 = models.ImageField(null=True, blank=True)
    photo3 = models.ImageField(null=True, blank=True)
    user_encoding1 = models.CharField(max_length=3000, verbose_name='User face encoding', null=True, blank=True)
    user_encoding2 = models.CharField(max_length=3000, verbose_name='User face encoding', null=True, blank=True)
    user_encoding3 = models.CharField(max_length=3000, verbose_name='User face encoding', null=True, blank=True)


class LateComer(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="User Fires Name", null=True, blank=True)
    last_name = models.CharField(max_length=200, verbose_name="User Last Name", null=True, blank=True)
    time_late = models.DateTimeField(null=True, blank=True)
