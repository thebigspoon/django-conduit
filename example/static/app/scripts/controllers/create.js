'use strict';

/**
 * @ngdoc function
 * @name conduitApp.controller:MainCtrl
 * @description
 * # CreateController
 * Controller of the conduitApp
 */
angular.module('conduitApp')
    .controller( 'CreateController', [ '$scope', '$http', '$log', function ( $scope, $http, $log ) {

        this.record = {
            bar : {} ,
            bazzes : [] ,
        };
        var self = this;

        this.sync = function() {
            $log.debug( "[ SYNCING... ]" );
            $http({method: 'POST', data: self.record, url: '/api/v1/foo/', })
                .success(function(data, status, headers, config) {
                    self.record = data;
                    $log.debug( "[ SUCCESS CREATE ]" );
                })
                .error(function(data, status, headers, config) {
                    $log.debug( "[ ERROR CREATE ]: ", status );
                });
        }

    }] );
