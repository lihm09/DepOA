from django.conf.urls import patterns, include, url

urlpatterns = patterns('doc.views',
    url(r'^$','index'),
    url(r'^addfile/$','add_file')
)