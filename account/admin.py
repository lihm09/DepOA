from django.contrib import admin
from account.models import UserProfile

class AccountAdmin(admin.ModelAdmin):
    model=UserProfile
    list_display = ("user","mobile","address","birthday","gender","QQ")
    radio_fields = {'gender':admin.VERTICAL}

admin.site.register(UserProfile, AccountAdmin)