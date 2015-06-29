from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class UserProfile(AbstractUser):
    class Meta(AbstractUser.Meta):
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    gender = models.CharField(max_length=1, choices=GENDER)
    birthday = models.DateField(null=True)
