from django.contrib import admin
from site_core.models import (Racket, Request, Upload, Comment, Rating,
                              Reputation)

admin.site.register(Racket)
admin.site.register(Request)
admin.site.register(Upload)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Reputation)
