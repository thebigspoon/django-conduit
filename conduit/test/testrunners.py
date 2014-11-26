try:
    from django.test.runner import DiscoverRunner as BaseRunner
except ImportError:
    # Django < 1.6 fallback
    from django.test.simple import DjangoTestSuiteRunner as BaseRunner
from django.utils.unittest import TestSuite
 
class GeoTestRunner( BaseRunner ):
    """
    only run geo related tests
    """

    def build_suite(self, *args, **kwargs):
        suite = super(GeoTestRunner, self).build_suite(*args, **kwargs)
        filtered_suite = TestSuite()
        filtered_suite.addTests( [ test for test in suite if test.__class__.__name__ == 'GeoMethodTestCase' ] )
        return filtered_suite


class StandardTestRunner( BaseRunner ):
    """
    for local development and quick "spot-checks" with the unit tests
    the installation, dependencies, permissions, and time required to set up Postgresql/PostGIS might be annoying.
    this test runner excludes geo related tests.
    """

    def build_suite(self, *args, **kwargs):
        suite = super(StandardTestRunner, self).build_suite(*args, **kwargs)
        filtered_suite = TestSuite()
        filtered_suite.addTests( [ test for test in suite if test.__class__.__name__ != 'GeoMethodTestCase' ] )
        return filtered_suite
 

