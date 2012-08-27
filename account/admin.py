from django.contrib import admin
from account.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user","student_number","grade","class_name","mobile","address","gender","birthday")
    radio_fields = {'gender':admin.HORIZONTAL}

admin.site.register(UserProfile,UserProfileAdmin)