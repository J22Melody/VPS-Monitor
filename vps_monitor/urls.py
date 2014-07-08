from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('vps_monitor.views',

    url(r'^login/$', 'login_view'),
    url(r'^logout/$', 'logout_view'),

    url(r'^$', 'index'),

    url(r'^get_os/$', 'get_os'),
    url(r'^get_mem/$', 'get_mem'), 

    url(r'^admin/', include(admin.site.urls)),
)
