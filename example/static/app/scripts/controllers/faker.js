'use strict';

/**
 * @ngdoc controller 
 * @name conduitApp.controller:FakeController
 * @description
 * # FakeController
 * Controller of the conduitApp that handles create UI
 */

var FakeController = function ( $scope, $log, CreateFooService, HtmlService ) {
    
    this.record = {
        defendant : "" ,
        servee : "yep yep" ,
        bar : {} ,
        bazzes : [] ,
    };
    this.$scope = $scope;
    this.$log = $log;
    this.$CreateFooService = CreateFooService;
    this.HtmlService = HtmlService;

};


//  DI
FakeController.$inject = [ '$scope', '$log', 'CreateFooService', 'HtmlService' ];


//  METHODS
FakeController.prototype.create_sync = function () {

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
angular.module('conduitApp').controller( 'FakeController', FakeController );
