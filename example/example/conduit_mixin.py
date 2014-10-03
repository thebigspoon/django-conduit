from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.models import Site
from django.core.context_processors import csrf
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response

import logging
logger = logging.getLogger(__file__)

from conduit.subscribe import subscribe, avoid, match
from example.models import Bar, Baz, Foo

def build_pub(self, request, *args, **kwargs):
    pub = []
    pub.append(request.method.lower())
    if kwargs.get(getattr(self.Meta, 'pk_field', 'id'), None):
        pub.append('detail')
    else:
        pub.append('list')
    kwargs['pub'] = pub
    return (request, args, kwargs)

@subscribe(sub=['get'])
def get_object(self, request, *args, **kwargs):
    pk_field_name = self.Meta.pk_field
    obj = self.Meta.model.objects.filter(**{pk_field_name: kwargs.get(pk_field_name, None)})
    if not obj.exists():
        raise Http404("cannot find {0} by pk_field = '{1}'".format(self.Meta.model, pk_field_name))
    kwargs['obj'] = obj[0]
    return (request, args, kwargs)

@subscribe(sub=['get', 'detail', 'list'])
def get_context_data(self, request, *args, **kwargs):
    context = {}
    if 'detail' in kwargs['pub']:
        context = {'foo': kwargs['obj']}
    elif 'list' in kwargs['pub']:
        context = {'foo_list': kwargs['queryset'],
         'is_conduit_view': True}
    kwargs['context_data'] = context
    return (request, args, kwargs)

def respond(self, request, *args, **kwargs):
    return render_to_response(self.Meta.template_name, kwargs.get('context_data', {}))

class ConduitBaseMixin(object):

    def build_pub(self, request, *args, **kwargs):
        pub = []
        pub.append(request.method.lower())
        if kwargs.get(getattr(self.Meta, 'pk_field', 'id'), None):
            pub.append('detail')
        else:
            pub.append('list')
        kwargs['pub'] = pub
        return (request, args, kwargs)


class ConduitMixin(ConduitBaseMixin):

    @subscribe(sub=[
     'post',
     'put',
     'delete',
     'head',
     'options',
     'trace'
    ])
    def reject_http_methods(self, request, *args, **kwargs):
        raise Http404("this URI does not handle any of the http methods \
                ['post', 'put', 'delete', 'head', 'options', 'trace']")

    @subscribe(sub=['get'])
    def get_object(self, request, *args, **kwargs):
        pk_field_name = self.Meta.pk_field
        obj = self.Meta.model.objects.filter(**{pk_field_name: kwargs.get(pk_field_name, None)})
        if not obj.exists():
            raise Http404("cannot find {0} by pk_field = '{1}'".format(self.Meta.model, pk_field_name))
        kwargs['obj'] = obj[0]
        return (request, args, kwargs)

    @subscribe(sub=['get'])
    def get_queryset(self, request, *args, **kwargs):
        if getattr(self.Meta, 'queryset', False):
            queryset = self.Meta.queryset
            if hasattr(queryset, '_clone'):
                queryset = queryset._clone()
        elif getattr(self.Meta, 'model', False):
            queryset = self.Meta.model._default_manager.all()
        else:
            raise ImproperlyConfigured("'%s' must define 'queryset' or 'model'" % self.__class__.__name__)
        kwargs['queryset'] = queryset
        return (request, args, kwargs)

    @subscribe(sub=['get', 'detail', 'list'])
    def get_context_data(self, request, *args, **kwargs):
        context = {}
        if 'detail' in kwargs['pub']:
            context = {'foo': kwargs['obj']}
        elif 'list' in kwargs['pub']:
            context = {'foo_list': kwargs['queryset'],
             'is_conduit_view': True}
        kwargs['context_data'] = context
        return (request, args, kwargs)

    def respond(self, request, *args, **kwargs):
        return render_to_response(self.Meta.template_name, kwargs.get('context_data', {}))


class ConduitFormMixin(ConduitBaseMixin):

    @subscribe(sub=[
         'put',
         'delete',
         'head',
         'options',
         'trace'
    ])
    def reject_http_methods(self, request, *args, **kwargs):
        raise Http404("this URI does not handle any of the http methods \
            ['post', 'put', 'delete', 'head', 'options', 'trace']")

    @subscribe(sub=['get'])
    def handle_http_get(self, request, *args, **kwargs):
        return (request, args, kwargs)

    @subscribe(sub=['post'])
    def handle_http_post(self, request, *args, **kwargs):
        logger.debug( "request.POST = %s" % request.POST )
        return (request, args, kwargs)

    @subscribe(sub=['get', 'post'])
    def get_form(self, request, *args, **kwargs):
        form_class = getattr(self.Meta, 'form_class', None)
        if not form_class:
            raise ImproperlyConfigured('the class {0} needs a Meta.form_class specified'.format(self.__class__.__name__))
        form_kwargs = {}
        if request.method in ('POST', 'PUT'):
            form_kwargs = self._get_form_kwargs(request)
        kwargs['form'] = form_class(**form_kwargs)
        return (request, args, kwargs)

    @subscribe(sub=['post'])
    def validate_form(self, request, *args, **kwargs):
        logger.debug('validate_form')
        form = kwargs['form']
        if form.is_valid():
            kwargs['form_is_valid'] = True
        else:
            kwargs['form_is_valid'] = False
        return (request, args, kwargs)

    @subscribe(sub=['post'])
    def set_success_url(self, request, *args, **kwargs):
        logger.debug('set_success_url')
        if kwargs['form_is_valid']:
            self.Meta.success_url = reverse('foo_conduit_list_view')
        return (request, args, kwargs)

    @subscribe(sub=['get', 'post'])
    def get_context_data(self, request, *args, **kwargs):
        logger.debug('get_context_data')
        context = {'form': kwargs['form']}
        kwargs['context_data'] = context
        return (request, args, kwargs)

    def respond(self, request, *args, **kwargs):
        logger.debug('respond')
        if kwargs.get('form_is_valid', None):
            return HttpResponseRedirect(self.Meta.success_url)
        return render_to_response(self.Meta.template_name, kwargs.get('context_data', {}))


class ConduitModelFormMixin(object):

    @subscribe(sub=['get', 'post'])
    def get_object(self, request, *args, **kwargs):
        pk_field_name = self.Meta.pk_field
        obj = self.Meta.model.objects.filter(**{pk_field_name: kwargs.get(pk_field_name, None)})
        if not obj.exists():
            raise Http404("cannot find {0} by pk_field = '{1}'".format(self.Meta.model, pk_field_name))
        kwargs['obj'] = obj[0]
        return (request, args, kwargs)

    @subscribe(sub=['get', 'post'])
    def get_form_class(self, request, *args, **kwargs):
        logger.debug('get_form_class')
        form_class = getattr(self.Meta, 'form_class', None)
        if not form_class:
            if getattr(self.Meta, 'model', None):
                model = self.Meta.model
            elif kwargs.get('obj', None) and kwargs['obj'] is not None:
                model = kwargs['obj'].__class__
            else:
                model = getattr(self.Meta, 'queryset').model if getattr(self.Meta, 'queryset', False) else None
            form_class = model_forms.modelform_factory(model)
        kwargs['form_class'] = form_class
        return (request, args, kwargs)

    @subscribe(sub=['get', 'post'])
    def get_form(self, request, *args, **kwargs):
        logger.debug('get_form')
        form_class = kwargs['form_class']
        
        form_kwargs = {}
        if request.method == 'GET':
            form_kwargs = {'instance': kwargs['obj']}
        elif request.method in [ 'PUT', 'POST' ]:
            form_kwargs = { 
                'data': request.POST ,
                'instance' : kwargs['obj']
            }
        kwargs['form'] = form_class(**form_kwargs)
        return (request, args, kwargs)

    @subscribe(sub=['post'])
    def validate_form(self, request, *args, **kwargs):
        logger.debug('validate_form')
        form = kwargs['form']
        if form.is_valid():
            kwargs['form_is_valid'] = True
            logger.debug('form is valid')
            updated_obj = form.save(commit=False)
            updated_obj.save()
            kwargs['form'] = kwargs['form_class'](**{'instance': updated_obj})
            kwargs['obj'] = updated_obj
        else:
            kwargs['form_is_valid'] = False
            logger.debug('form is not valid')
            logger.debug( "form errors = %s" % form.errors )
        return (request, args, kwargs)



