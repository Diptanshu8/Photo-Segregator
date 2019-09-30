(function () {

  angular.module('PhotoSegregatorApp', [])

  .controller('PhotoScanController', ['$scope', '$log',
    function($scope, $log) {
    $scope.selected = [];

    $scope.scanImages = function() {
        $.each($("input[name='cb']:checked"), function(){            
                            $scope.selected.push($(this).attr('id'));
                        });
        $log.log("My checked images are: " + $scope.selected.join(", "));
        $scope.selected = [];
        };
    }
  ]);
}());

