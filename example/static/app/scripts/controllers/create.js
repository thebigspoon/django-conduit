'use strict';

/**
 * @ngdoc controller 
 * @name conduitApp.controller:CreateController
 * @description
 * # CreateController
 * Controller of the conduitApp that handles create UI
 */

var CreateController = function ( $scope, $log, CreateFooService ) {
    
    this.record = {
        bar : {} ,
        bazzes : [] ,
    };
    this.$scope = $scope;
    this.$log = $log;
    this.$CreateFooService = CreateFooService;

};


//  DI
CreateController.$inject = [ '$scope', '$log', 'CreateFooService' ];


//  METHODS
CreateController.prototype.create_sync = function () {

        this.$log.debug( "[ CREATE SYNCING ]" );
        this.$CreateFooService.sync( this.record )
            .success(function(data, status, headers, config) {

                this.record = data;
                this.$log.debug( "[ SUCCESS CREATE ]", this.data );

            }.bind(this))
            .error(function(data, status, headers, config) {

                this.$log.debug( "[ ERROR CREATE ]: ", status );

            }.bind(this));

};


//  REGISTER
angular.module('conduitApp').controller( 'CreateController', CreateController );
