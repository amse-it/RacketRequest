from django.contrib import admin
from site_core.models import (Racket, Request, Upload, Comment, Rating,
                              Reputation)


class RequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'has_expired')
    list_filter = ['created']
    search_fields = ['question_text']

admin.site.register(Racket)
admin.site.register(Request, RequestAdmin)
admin.site.register(Upload)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Reputation)
