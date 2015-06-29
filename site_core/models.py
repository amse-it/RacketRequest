from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation)
from django.contrib.contenttypes.models import ContentType


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


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, default=None)
    object_id = models.PositiveIntegerField(default=None)
    content_object = GenericForeignKey('content_type', 'object_id')
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    remove = models.BooleanField(default=False)

    def __unicode__(self):
        return self.comment


class Upload(models.Model):
    content_type = models.ForeignKey(ContentType, default=None)
    object_id = models.PositiveIntegerField(default=None)
    content_object = GenericForeignKey('content_type', 'object_id')
    path = models.URLField()
    title = models.CharField(max_length=50)
    type = models.IntegerField(choices=FILE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    remove = models.BooleanField(default=False)


class Request(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    remove = models.BooleanField(default=False)
    comments = GenericRelation(Comment)
    uploads = GenericRelation(Upload)

    @property
    def get_expiry(self):
        pass

    def __unicode__(self):
        return self.title


class Racket(models.Model):
    request = models.ForeignKey(Request)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_started = models.DateField()
    created = models.DateField(auto_now_add=True)
    remove = models.BooleanField(default=False)
    comments = GenericRelation(Comment)
    uploads = GenericRelation(Upload)

    def __unicode__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    racket = models.ForeignKey(Racket)
    #star rating maximum 5
    score = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    remove = models.BooleanField(default=False)


class Reputation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='reputations'
    )
    referral = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_credible = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    remove = models.BooleanField(default=False)
