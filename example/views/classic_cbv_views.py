#
#  django imports
#
from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.models import Site
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.views.generic.detail import BaseDetailView, DetailView
from django.views.generic.list import BaseListView, ListView
from django.views.generic.edit import FormView

#
#  sys imports
#
import logging
logger = logging.getLogger( __file__ )

#
#  app imports
#
from example.models import Bar, Baz, Foo

class FooDetailView( DetailView ):
    model = Foo
    context_object_name = 'foo'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    template_name = 'foo_detail_view.html'

class FooListView( ListView ):
    model = Foo
    context_object_name = 'foo_list'
    template_name = 'foo_list_view.html'

