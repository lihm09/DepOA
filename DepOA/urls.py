from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'DepOA.views.index'),
    # url(r'^DepOA/', include('DepOA.foo.urls')),
    url(r'^media/(.*)$', 'django.views.static.serve',{'document_root':'./media'}),
    url(r'^grappelli/',include('grappelli.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/',include('account.urls')),
    url(r'^doc/',include('doc.urls')),
    url(r'^org/',include('org.urls'))
)
