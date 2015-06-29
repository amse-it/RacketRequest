from django.db import models
from django.conf import settings
from site_core.models import BaseModel
# Create your models here.

class Thread(BaseModel):
	title = models.CharField(max_length=50)

	def __unicode__(self):
		return self.title


class Message(BaseModel):
	thread = models.ForeignKey(Thread)
	sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='messages_sent', default=None)
	receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='messages_received', default=None)
	content = models.TextField()
	receiver_visible = models.BooleanField(default=True)
	sender_visible = models.BooleanField(default=True)

	def __unicode__(self):
		return self.thread.title + ':' + self.content[0:10]
