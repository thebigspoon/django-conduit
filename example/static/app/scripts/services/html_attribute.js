'use strict';

/**
 * @ngdoc controller 
 * @name conduitApp.controller:HtmlService
 * @description
 * # HtmlService
 * Mixin that handles adding attributes to inputs
 */

var HtmlService = function ( $log ) {

    this.$log = $log;
    
};


//  DI
HtmlService.$inject = [ '$log' ];


//  METHODS
HtmlService.prototype.add_required_attributes = function ( scope_context, element, attr ) {

        if ( typeof scope_context === 'undefined' || scope_context === null || scope_context === '' ) {
            throw Error( "scope context cannot be empty or undefined" );
        }

        /*
        **
        **  REQUIRED
        **
        */
        if ( !attr.zDataLabel ) {
            throw Error( "z-data-label is a required attribute" );
        }
        scope_context.ztext_label = attr.zDataLabel;

        if ( !attr.zDataId ) {
            throw Error( "z-data-id is a required attribute" );
        }
        scope_context.zid = attr.zDataId;
    

};

HtmlService.prototype.add_optional_attributes = function ( scope_context, element, attr ) {

        if ( typeof scope_context === 'undefined' || scope_context === null || scope_context === '' ) {
            throw Error( "scope context cannot be empty or undefined" );
        }

        /*
        **
        **  OPTIONAL
        **
        */
        if ( attr.zDataName ) { 
            element.find( 'input' ).attr( 'name',  attr.zDataName );
        }
        if ( attr.zDataPlaceholder ) { 
            element.find( 'input' ).attr( 'placeholder',  attr.zDataPlaceholder );
        }

        if ( attr.zDataRequired ) { 
            element.find( 'input' ).attr( 'required', 'required' );
        }

        if ( attr.zDataDisabled ) { 
            element.find( 'input' ).attr( 'disabled', 'disabled' );
        }

        if ( attr.zDataReadonly ) { 
            element.find( 'input' ).attr( 'readonly', 'readonly' );
        }

};


//  REGISTER
angular.module('conduitApp').service( 'HtmlService', HtmlService );
