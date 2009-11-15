from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^polls/', include('pollngo.urls')),
    )

urlpatterns += patterns('',
    (r'^admin/(.*)', admin.site.root),
    )

if settings.DEBUG:    
    media_dir = settings.MEDIA_ROOT
    urlpatterns += patterns('',
            url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': media_dir}),
        )