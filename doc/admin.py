from django.contrib import admin
from doc.models import DocPub

class DocPubAdmin(admin.ModelAdmin):
    list_display = ("file_name","file_path","org","upload_time")

admin.site.register(DocPub,DocPubAdmin)