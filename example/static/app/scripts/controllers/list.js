'use strict';

/**
 * @ngdoc function
 * @name conduitApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the conduitApp
 */
angular.module('conduitApp')
    .controller( 'ListController', [ $http, $log, function ( $http, $log ) {

        this.data = [];
        var self = this;

        // get all foo objects
        $http({method: 'GET', url: '/api/v1/foo/'}).
            success(function(data, status, headers, config) {
                self.data = data;
                $log.debug( "[ SUCCESS ]" );
            }).
            error(function(data, status, headers, config) {
                $log.debug( "[ ERROR ]: ", status );
            });

    }] );
