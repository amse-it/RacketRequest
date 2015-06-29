from django.contrib import admin
from messaging.models import (Thread, Message)

# Register your models here.
admin.site.register(Thread)
admin.site.register(Message)