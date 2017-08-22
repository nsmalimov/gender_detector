myApp.controller('modalController', ['$scope', 'close', function($scope, close) {

  //$scope.markdown = "### python";
  $scope.close = function() {
 	  close('', 500); // close, but give 500ms for bootstrap to animate
  };

}]);