from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DepOA.views.home', name='home'),
    # url(r'^DepOA/', include('DepOA.foo.urls')),
    url(r'^media/(.*)$', 'django.views.static.serve',{'document_root':'./media'}),
    url(r'^grappelli/',include('grappelli.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^doc/',include('doc.urls')),
    url(r'^org/',include('org.urls'))
)
