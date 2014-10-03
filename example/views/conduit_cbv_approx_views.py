#
#  django imports
#
from django import forms
from django.conf import settings
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.views.generic.edit import FormMixin

#
#  sys imports
#
import logging
logger = logging.getLogger( __file__ )

#
#  app imports
#
from example.models import Bar, Baz, Foo
from example.forms import NormalForm, FooForm
from example.conduit_mixin import ConduitMixin
from conduit import Conduit
from conduit.subscribe import subscribe, avoid, match

class FooConduitDetail( Conduit ):

    class Meta:
        conduit = (
            'example.conduit_mixin.ConduitBaseMixin.build_pub',
            'example.conduit_mixin.ConduitMixin.reject_http_methods',
            'example.conduit_mixin.ConduitMixin.get_object',
            'example.conduit_mixin.ConduitMixin.get_context_data',
            'example.conduit_mixin.ConduitMixin.respond',
        )
        model = Foo
        template_name = 'foo_detail_view.html'
        pk_field = 'id'
        
class FooConduitList( Conduit ):

    class Meta:
        conduit = (
            'example.conduit_mixin.ConduitBaseMixin.build_pub',
            'example.conduit_mixin.ConduitMixin.reject_http_methods',
            'example.conduit_mixin.ConduitMixin.get_queryset',
            'example.conduit_mixin.ConduitMixin.get_context_data',
            'example.conduit_mixin.ConduitMixin.respond',
        )
        model = Foo
        template_name = 'foo_list_view.html'


class FooConduitFormView( Conduit ):

    class Meta:
        conduit = (
            'example.conduit_mixin.ConduitBaseMixin.build_pub',
            'example.conduit_mixin.ConduitFormMixin.reject_http_methods',
            'example.conduit_mixin.ConduitFormMixin.handle_http_get',
            'example.conduit_mixin.ConduitFormMixin.handle_http_post',
            'example.conduit_mixin.ConduitFormMixin.get_form',
            'example.conduit_mixin.ConduitFormMixin.validate_form',
            'example.conduit_mixin.ConduitFormMixin.set_success_url',
            'example.conduit_mixin.ConduitFormMixin.get_context_data',
            'example.conduit_mixin.ConduitFormMixin.respond',
        )
        model = Foo
        template_name = 'foo_normal_form_view.html'
        form_class = NormalForm
        success_url = None 

    def _get_form_kwargs( self, request ):
        form_kwargs = {
            'initial': getattr( self.Meta, 'initial', {} )
        }
        form_kwargs.update({
            'data': request.POST,
            'files': request.FILES,
        })
        return form_kwargs


class FooConduitModelFormUpdate( Conduit ):

    class Meta:
        conduit = (
            'example.conduit_mixin.ConduitBaseMixin.build_pub',
            'example.conduit_mixin.ConduitFormMixin.reject_http_methods',
            'example.conduit_mixin.ConduitModelFormMixin.get_object',
            'example.conduit_mixin.ConduitFormMixin.handle_http_get',
            'example.conduit_mixin.ConduitFormMixin.handle_http_post',
            'example.conduit_mixin.ConduitModelFormMixin.get_form_class',
            'example.conduit_mixin.ConduitModelFormMixin.get_form',
            'example.conduit_mixin.ConduitModelFormMixin.validate_form',
            'example.conduit_mixin.ConduitFormMixin.set_success_url',
            'example.conduit_mixin.ConduitFormMixin.get_context_data',
            'example.conduit_mixin.ConduitFormMixin.respond',
        )
        pk_field = 'id'
        model = Foo
        template_name = 'foo_normal_form_view.html'
        form_class = FooForm
        success_url = None 


class FooTestFunc( Conduit ):

    class Meta:
        conduit = (
            'example.conduit_mixin.build_pub',
            'example.conduit_mixin.get_object',
            'example.conduit_mixin.get_context_data',
            'example.conduit_mixin.respond',
        )
        model = Foo
        template_name = 'foo_detail_view.html'
        pk_field = 'id'

class FooTestClassicMixin( Conduit, ConduitMixin ):

    class Meta:
        conduit = (
            'build_pub',
            'get_object',
            'get_context_data',
            'respond',
        )
        model = Foo
        template_name = 'foo_detail_view.html'
        pk_field = 'id'

class FooTestClassicMixinExplicit( Conduit, ConduitMixin ):

    class Meta:
        conduit = (
            'example.conduit_mixin.ConduitMixin.build_pub',
            'example.conduit_mixin.ConduitMixin.get_object',
            'example.conduit_mixin.ConduitMixin.get_context_data',
            'example.conduit_mixin.ConduitMixin.respond',
        )
        model = Foo
        template_name = 'foo_detail_view.html'
        pk_field = 'id'

class FooTestRecommended( Conduit ):

    class Meta:
        conduit = (
            'example.conduit_mixin.ConduitMixin.build_pub',
            'example.conduit_mixin.ConduitMixin.get_object',
            'example.conduit_mixin.ConduitMixin.get_context_data',
            'example.conduit_mixin.ConduitMixin.respond',
        )
        model = Foo
        template_name = 'foo_detail_view.html'
        pk_field = 'id'


