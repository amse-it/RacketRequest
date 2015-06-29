from django.contrib import admin
from django.contrib.auth.models import User
from site_core.models import (Racket, Request, Upload, Comment, Rating,
                              Reputation, UserProfile)


class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Login Fields', {'fields': [
            'username',
            'password',
        ]}),
        ('Personal Information', {'fields': [
            'first_name',
            'last_name',
            'gender',
            'birthday',
        ]}),
        ('Privileges', {'fields': [
            'is_superuser', 'is_staff', 'groups', 'user_permissions'
        ], 'classes': ['collapse']}),
        ('Record Information', {'fields': [
            'date_joined',
            'is_active',
        ], 'classes': ['collapse']}),
    )

admin.site.unregister(User)
admin.site.register(UserProfile, UserAdmin)

admin.site.register(Racket)
admin.site.register(Request)
admin.site.register(Upload)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Reputation)
