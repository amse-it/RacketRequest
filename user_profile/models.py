from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class UserProfile(User):
    class Meta(User.Meta):
        verbose_name = 'UserProfile'

    gender = models.CharField(max_length=1, choices=GENDER)
    birthday = models.DateField()
