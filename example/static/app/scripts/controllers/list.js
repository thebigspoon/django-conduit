'use strict';

/**
 * @ngdoc function
 * @name conduitApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the conduitApp
 */
angular.module('conduitApp')
    .controller( 'ListController', [ '$scope', '$http', '$log', function ( $scope, $http, $log ) {

        this.data = [];
        var self = this;

        // get all foo objects
        $http({method: 'GET', url: '/api/v1/foo/?order_by=-created'}).
            success(function(data, status, headers, config) {
                self.data = data;
                $log.debug( "[ SUCCESS LIST ]" );
            }).
            error(function(data, status, headers, config) {
                $log.debug( "[ ERROR ]: ", status );
            });

    }] );
