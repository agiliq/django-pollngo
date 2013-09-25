from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('pollngo.views',
    url(r'^$', 'index', name='pollngo_index'),
    url(r'^poll/(?P<slug>[^\.^/]+)/$', 'question', name='pollngo_question'),
    url(r'^create/$', 'create', name='pollngo_create'),
    url(r'^help/$', 'help', name='pollngo_help'),
    url(r'^results/(?P<slug>[^\.^/]+)/$', 'results', name='pollngo_results'),
    )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)