from django.contrib import admin
from doc.models import DocPub

class DocPubAdmin(admin.ModelAdmin):
    list_display = ("file_name","org","upload_time")

admin.site.register(DocPub,DocPubAdmin)