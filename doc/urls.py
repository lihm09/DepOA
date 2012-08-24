from django.conf.urls import patterns, include, url

urlpatterns = patterns('doc.views',
    url(r'^$','index')
)