'use strict';

/**
 * @ngdoc function
 * @name conduitApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the conduitApp
 */
angular.module('conduitApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
