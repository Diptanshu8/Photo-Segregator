(function () {

  'use strict';

  angular.module('PhotoSegregatorApp', [])

  .controller('PhotoScanController', ['$scope', '$log', '$http', '$timeout',
    function($scope, $log, $http, $timeout) {
	$scope.img = ""
    $scope.scanImage = function(value) {

      $log.log("Inside scanImage");

      // get the URL from the input
      var userInput = $scope.img;

      // fire the API request
      $http.post('/scan_image', {"img": userInput}).
        success(function(results) {
          $log.log(value);
          $log.log(userInput);
        }).
        error(function(error) {
          $log.log(error);
        });
    };
  }
  ]);
}());

