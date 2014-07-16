from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
handler404 = 'myfirstapp1.views.custom_404'
handler500 = 'myfirstapp1.views.custom_404'

urlpatterns = patterns('',    
    #(r'^$', 'touritz_app.views.main'),
    url(r'^app/', include('myfirstapp1.urls')),
    
    # Examples:
    # url(r'^$', 'myproject1.views.home', name='home'),
    # url(r'^myproject1/', include('myproject1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
