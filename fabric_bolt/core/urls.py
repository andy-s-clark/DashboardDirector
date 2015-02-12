from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
import socketio.sdjango

from fabric_bolt.core import views


socketio.sdjango.autodiscover()

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^', include('fabric_bolt.accounts.urls')),
    url(r'^$', views.Dashboard.as_view(), name='index'),
    url(r'^hosts/', include('fabric_bolt.hosts.urls')),
    url(r'^web-hooks/', include('fabric_bolt.web_hooks.urls')),
    url(r'^launch-window/', include('fabric_bolt.launch_window.urls')),
    url(r'^projects/', include('fabric_bolt.projects.urls')),
    url("^socket\.io", include(socketio.sdjango.urls)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
)

urlpatterns += i18n_patterns(
    '',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/docs/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# Serve the static files from django
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
