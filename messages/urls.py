from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('messages.views',
    url(r'^$',message),
)
