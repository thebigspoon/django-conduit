from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:

#
#  classic CBV imports
#
from example.views import FooDetailView
from example.views import FooListView
from example.views import FooConduitFormView
from example.views import FooConduitModelFormUpdate
from example.views import FooTestFunc, FooTestClassicMixin, FooTestClassicMixinExplicit, FooTestRecommended
#
#  conduit CBV imports
#
from example.views import FooConduitDetail
from example.views import FooConduitList

urlpatterns = patterns('',

    #
    #  conduit CBV approximations
    #
    url(r'^conduit/foo/(?P<id>.*)/$', FooConduitDetail().view, name='foo_conduit_detail_view'),
    url(r'^conduit/foo/$', FooConduitList().view, name='foo_conduit_list_view'),
    url(r'^conduit/forms/normal/foo/$', FooConduitFormView().view, name='foo_conduit_normal_form_view'),
    url(r'^conduit/model/foo/update/(?P<id>.*)/$', FooConduitModelFormUpdate().view, name='foo_conduit_model_form_update_view'),

    url(r'^test/foo/1/(?P<id>.*)/$', FooTestFunc().view, name='foo_test_func'),
    url(r'^test/foo/2/(?P<id>.*)/$', FooTestClassicMixin().view, name='foo_test_classic'),
    url(r'^test/foo/3/(?P<id>.*)/$', FooTestClassicMixinExplicit().view, name='foo_test_classic_explicit'),
    url(r'^test/foo/4/(?P<id>.*)/$', FooTestRecommended().view, name='foo_test_recommended'),

    #
    #  classic CBV implementations
    #
    url(r'^foo/(?P<pk>.*)/$', FooDetailView.as_view(), name='foo_detail_view'),
    url(r'^foo/$', FooListView.as_view( template_name="foo_list_view.html" ), name='foo_list_view'),

    #
    #  REST api
    #
    url(r'^api/', include('api.urls')),
)
