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
      .when('/edit/:resource_id/', {
        templateUrl: 'views/edit.html',
        controller: 'EditController'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
