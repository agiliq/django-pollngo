from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template



urlpatterns = patterns('pollngo.views',
    url(r'^$', 'index', name='pollngo_index'),
    url(r'^poll/(?P<slug>[^\.^/]+)/$', 'question', name='pollngo_question'),
    url(r'^create/$', 'create', name='pollngo_create'),
    url(r'^help/$', 'help', name='pollngo_help'),
    url(r'^results/(?P<slug>[^\.^/]+)/$', 'results', name='pollngo_results'),
    )