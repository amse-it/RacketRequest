from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Login Fields', {'fields': [
            'username',
            'password',
        ]}),
        ('Personal Information', {'fields': [
            'first_name',
            'last_name',
            'email',
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

admin.site.register(UserProfile, UserProfileAdmin)
