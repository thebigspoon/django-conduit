from django import forms
from django.utils.translation import ugettext_lazy as _

import re
import logging
logger = logging.getLogger( __file__ )

from example.models import Foo, Bar

class FooForm(forms.ModelForm):
    class Meta:
        model = Foo
        exclude = [
            #'bar',
            #'bazzes',
            'file_field',
        ]


class BarForm(forms.ModelForm):
    class Meta:
        model = Bar


class NormalForm(forms.Form):

    name = forms.CharField( label=_('Name' ), required = True )
    text = forms.CharField( label=_('Text' ), required = True)
    float_field = forms.FloatField( label=_('Float Field' ), required = True)
    boolean = forms.BooleanField( label=_('Bool Field' ), required = True)
    birthday = forms.DateTimeField( label=_('Birthday' ), required = True)
    decimal = forms.DecimalField( label=_('Decimal' ), required = True)
     
    def __init__( self, *args, **kwargs ):
        super( NormalForm, self ).__init__( *args, **kwargs )

    def clean( self ):
        cleaned_data = self.cleaned_data
        return cleaned_data

    def clean_name( self ):
        cleaned_field_data = self.cleaned_data['name']

        #   
        #  validate that the name
        #  only has letters and numbers
        #   
        pattern = re.compile('[^a-zA-Z0-9]')
        match = pattern.findall( cleaned_field_data )
        logger.debug( "name field match %s" % match )
        if len( match ) > 0:
            raise forms.ValidationError( 'the name can only contain letters and numbers' )

        #   
        #  validate that the
        #  name is the right length
        #   
        logger.debug( "name field length = %i" % len( cleaned_field_data ) ) 
        if len( cleaned_field_data ) > 25: 
            raise forms.ValidationError( 'the name field can  only be 25 characters, you have %i' % len( cleaned_field_data ) )

        return cleaned_field_data

