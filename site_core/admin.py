from django.contrib import admin
from django.contrib.auth.models import User
from site_core.models import (Racket, Request, Upload, Comment, Rating,
    Reputation, UserProfiles)

admin.site.unregister(User)
admin.site.register(UserProfiles)

admin.site.register(Racket)
admin.site.register(Request)
admin.site.register(Upload)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Reputation)
