from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation)
from django.contrib.contenttypes.models import ContentType

import datetime

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


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    remove = models.BooleanField(default=False)


class Comment(BaseModel):
    content_type = models.ForeignKey(ContentType, default=None)
    object_id = models.PositiveIntegerField(default=None)
    content_object = GenericForeignKey('content_type', 'object_id')
    comment = models.TextField()

    def __unicode__(self):
        return self.comment


class Upload(BaseModel):
    content_type = models.ForeignKey(ContentType, default=None)
    object_id = models.PositiveIntegerField(default=None)
    content_object = GenericForeignKey('content_type', 'object_id')
    path = models.URLField()
    title = models.CharField(max_length=50)
    type = models.IntegerField(choices=FILE_TYPE)


class Request(BaseModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField(default=1)
    comments = GenericRelation(Comment)
    uploads = GenericRelation(Upload)

    @property
    def expiry(self):
        return self.created + datetime.timedelta(days=self.duration)

    def __unicode__(self):
        return self.title


class Racket(BaseModel):
    request = models.ForeignKey(Request)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_started = models.DateField()
    comments = GenericRelation(Comment)
    uploads = GenericRelation(Upload)

    def __unicode__(self):
        return self.title


class Rating(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    racket = models.ForeignKey(Racket)
    # star rating maximum 5
    score = models.IntegerField(default=0)


class Reputation(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='reputations'
    )
    referral = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_credible = models.BooleanField()
