from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'umum.views.depan', name='um_depan'),
    
    # url(r'^diskas/', include('diskas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #django
    url(r'^admin/', include(admin.site.urls)),
)
