from django import get_version
from distutils.version import StrictVersion

from .views import SwaggerView, ResourcesView, SchemaView

try:
	from django.conf.urls import url
except ImportError:
	from django.conf.urls.defaults import url

# RemovedInDjango110Warning: 
# django.conf.urls.patterns() is deprecated removed in Django 1.10. 
# Update your urlpatterns to be a list of django.conf.urls.url() instances instead.
urlpatterns = [
    url(r'^$', SwaggerView.as_view(), name='index'),
    url(r'^resources/$', ResourcesView.as_view(), name='resources'),
    url(r'^schema/(?P<resource>\S+)$', SchemaView.as_view()),
    url(r'^schema/$', SchemaView.as_view(), name='schema')
]

if StrictVersion(get_version()) <= StrictVersion('1.8'):
	urlpatterns = patterns('', *urlpatterns)
