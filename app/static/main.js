(function () {

  angular.module('PhotoSegregatorApp', [])

  .controller('PhotoScanController', ['$scope', '$log',
    function($scope, $log) {

    $scope.test = function() {
        alert("INside JS function");
            //$.each($("input:checked"), function(){            
                        //    $scope.selected.push($(this).id());
            //            alert("My checked images are: " + $(this.id()));
             //           });
    };

	$scope.test_image = function() {
		alert("SKRILL hit image callback");
  }
  ]);
}());

