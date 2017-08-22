myApp.controller('pageslideCtrl', ['$scope', function ($scope) {

    $scope.checked = false;
    $scope.size = '100px';

    $scope.toggle = function () {
        $scope.checked = !$scope.checked
    };

    $scope.mockRouteChange = function () {
        $scope.$broadcast('$locationChangeStart');
    };

    $scope.onopen = function () {
        alert('Open');
        console.log(this, $scope);
    };

    $scope.onclose = function () {
        alert('Close');
        console.log($scope);
    }
}]);