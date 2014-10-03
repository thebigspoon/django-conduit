'use strict';

/**
 * @ngdoc overview
 * @name conduitApp
 * @description
 * # conduitApp
 *
 * Main module of the application.
 */
angular
  .module('conduitApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/list.html',
        controller: 'ListController'
      })
      .when('/create', {
        templateUrl: 'views/create.html',
        controller: 'CreateController'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
