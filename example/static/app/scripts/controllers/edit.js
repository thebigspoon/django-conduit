'use strict';

/**
 * @ngdoc controller 
 * @name conduitApp.controller:EditController
 * @description
 * # EditController
 * Controller of the conduitApp that handles create UI
 */

var EditController = function ( $scope, $log, $routeParams, EditFooService ) {
    
    this.params = {};
    this.record = {};
    this.$scope = $scope;
    this.$routeParams = $routeParams;
    this.$log = $log
    this.$EditFooService = EditFooService;

    // sync data
    this.edit_sync();

};


//  DI
EditController.$inject = [ '$scope', '$log', '$routeParams', 'EditFooService' ];


//  METHODS
EditController.prototype.edit_sync = function () {

        this.$log.debug( "[ EDIT SYNCING ]" );
        this.$EditFooService.sync( this.$routeParams.resource_id, this.params )
            .success(function(data, status, headers, config) {

                this.record = data;
                this.$log.debug( "[ SUCCESS EDIT ]", this.record );

            }.bind(this))
            .error(function(data, status, headers, config) {

                this.$log.debug( "[ ERROR EDIT ]: ", status );

            }.bind(this));

};


//  REGISTER
angular.module('conduitApp').controller( 'EditController', EditController );
