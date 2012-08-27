from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'DepOA.views.index'),
    url(r'^media/(.*)$', 'django.views.static.serve',{'document_root':'./media'}),
    url(r'^upload/(.*)$', 'django.views.static.serve',{'document_root':'./upload'}),

    url(r'^grappelli/',include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/',include('account.urls')),
    url(r'^doc/',include('doc.urls')),

    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^logout/$','django.contrib.auth.views.logout_then_login')
)
