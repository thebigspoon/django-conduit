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

        var typedef =  'TEXTINPUT';

        $log.info( "[ INSTANTIATE ]: ", attr.zDataName );
        $log.debug( "[ SCOPE ]: ", scope );
        $log.debug( "[ CONTROLLERS ]: ", controllers );
        $log.debug( "[ ATTRS ]: ", attr );

        //  setup controllers
        var model_controller = controllers[0];
        var form_controller = controllers[1];


        /*
        **
        **  REQUIRED
        **
        */
        form_controller.HtmlService.add_required_attributes( scope, element, attr );


        /*
        **
        **  OPTIONAL
        **
        */
        form_controller.HtmlService.add_optional_attributes( scope, element, attr );


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
