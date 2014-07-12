from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('vps_monitor.views',

    url(r'^login/$', 'login_view'),
    url(r'^logout/$', 'logout_view'),

    url(r'^$', 'index'),

    url(r'^get_info/$', 'get_info'),

    url(r'^admin/', include(admin.site.urls)),
)
