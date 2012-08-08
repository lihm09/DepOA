from django.conf.urls import patterns, include, url

urlpatterns = patterns('account.views',
    url(r'^login/$','login_view'),
    url(r'^logout/$','logout_view')
)