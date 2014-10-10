'use strict';

/**
 * @ngdoc service 
 * @name conduitApp.service:CreateFooService
 * @description
 * # CreateFooService
 * a service for POST -> CREATE
 */

var CreateFooService = function ( $http, $log ) {

    this.url = '/api/v1/foo/';
    this.$http = $http;
    this.$log = $log;

};


//  METHODS
CreateFooService.prototype.sync = function( params ) {

    this.$log.debug( "[ CREATE FOO ]" );

    return this.$http( {method: 'POST', data: params, url: this.url } );

};


//  DI
CreateFooService.$inject = [ '$http', '$log' ];



//  REGISTER
angular.module('conduitApp').service( 'CreateFooService', CreateFooService );
