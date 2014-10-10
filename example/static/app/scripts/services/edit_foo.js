'use strict';
/**
 * @ngdoc service 
 * @name conduitApp.service:EditFooService
 * @description
 * # EditFooService
 * a service for POST -> CREATE
 */

var EditFooService = function ( $http, $log ) {

    this.url = '/api/v1/foo/';
    this.$http = $http;
    this.$log = $log;

};


//  METHODS
EditFooService.prototype.sync = function( resource_id, params ) {

    this.$log.debug( "[ CREATE FOO ]" );

    return this.$http( {method: 'GET', data: params, url: ( this.url + resource_id + '/' ) } );

};


//  DI
EditFooService.$inject = [ '$http', '$log' ];



//  REGISTER
angular.module('conduitApp').service( 'EditFooService', EditFooService );
