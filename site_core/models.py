from django.db import models
from django.contrib.auth.models import User


FILE_TYPE = (
    (0, 'Video'),
    (1, 'Audio'),
    (2, 'Image'),
    (3, 'Text'),
)

MODEL_TARGET = (
    (0, 'Request'),
    (1, 'Racket'),
)

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class UserProfile(User):
    class Meta:
        verbose_name = 'UserProfile'
        
    gender = models.CharField(max_length=1, choices=GENDER)
    birthday = models.DateField()


class Request(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    remove = models.BooleanField(default=False)

    @property
    def get_expiry(self):
        pass


class Racket(models.Model):
    request = models.ForeignKey(Request)
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_started = models.DateField()
    created = models.DateField(auto_now_add=True)
    remove = models.BooleanField(default=False)


class Comment(models.Model):
    #0 = Request, 1 = Racket
    category = models.IntegerField(choices=MODEL_TARGET)
    #request_id or racket_id
    category_id = models.IntegerField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    remove = models.BooleanField(default=False)


class Rating(models.Model):
    user = models.ForeignKey(User)
    racket = models.ForeignKey(Racket)
    #star rating maximum 5
    score = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    remove = models.BooleanField(default=False)


class Upload(models.Model):
    category = models.IntegerField(choices=MODEL_TARGET)
    category_id = models.IntegerField()
    path = models.URLField()
    title = models.CharField(max_length=50)
    type = models.IntegerField(choices=FILE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    remove = models.BooleanField(default=False)


class Reputation(models.Model):
    user = models.ForeignKey(User, related_name='reputations')
    referral = models.ForeignKey(User)
    is_credible = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    remove = models.BooleanField(default=False)
