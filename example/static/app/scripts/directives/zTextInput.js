'use strict';

/**
 * @ngdoc directive
 * @name conduitApp.controllers:zTextinput
 * @description
 * # zTextinput
 * Controller of the conduitApp that handles create UI
 */

var zTextinput = function ( $document, $log ) {

    var linker_def = function( scope, element, attr, controllers ) { 

        $log.info( "[ INSTANTIATE ]: ", attr.zDataName );
        $log.debug( "[ SCOPE ]: ", scope );
        $log.debug( "[ CONTROLLERS ]: ", controllers );
        $log.debug( "[ ATTRS ]: ", attr );

        //  setup controllers
        var model_controller = controllers[0];
        var form_controller = controllers[1];


        // labeling
        if ( attr.zDataLabel ) {
            scope.ztext_label = attr.zDataLabel;
        }

        //  arg(s) added to inputs
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


        // update the view with the model_controller's model value
        model_controller.$render = function() {
            element.find( 'input' ).val( model_controller.$viewValue );
        };

        var list = function() {
            $log.debug( "[ LIST ]: ",  model_controller.$viewValue );
            $log.debug( model_controller );
            //model_controller.$setViewValue( value );
        };

        element.find( 'input' ).on( 'keyup', function( e ) {
            $log.debug( "[ VALUE ]: ", e.target.value );
            model_controller.$setViewValue( e.target.value );
            list();
        });

        model_controller.$render();  // intialize and render first time

    };


    return {

        restrict : 'E' ,
        require : [ 'ngModel', '^ngController' ] ,
        scope : { } , 
        templateUrl : 'views/z-textinput.html' ,
        link : linker_def ,

    };

};


    

//  DI
zTextinput.$inject = [ '$document', '$log' ];


//  REGISTER
angular.module('conduitApp').directive( 'zTextinput', zTextinput );
