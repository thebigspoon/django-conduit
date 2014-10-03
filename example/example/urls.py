from django.conf.urls import patterns, include, url
from django.conf import settings
import os

urlpatterns = patterns('',
    url( r'^css/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/css' % os.path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^dist/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/dist' % os.path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^app/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/app' % os.path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^bower_components/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/bower_components' % os.path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^font/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/font'% os.path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^img/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/img' % os.path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/' % os.path.join( settings.ABSOLUTE_PATH, 'media' ).replace('\\','/') } ),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/' % os.path.join( settings.ABSOLUTE_PATH, 'static' ).replace('\\','/') } ),
    url( r'^js/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/js' % os.path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),

    url(r'^api/', include('api.urls')),
)
