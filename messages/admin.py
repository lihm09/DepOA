from django.contrib import admin
from messages.models import Situation,Message

class SituationAdmin(admin.ModelAdmin):
    list_display = ("name","time")

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','time','ip','situation','title','content')

admin.site.register(Situation,SituationAdmin)
admin.site.register(Message,MessageAdmin)



