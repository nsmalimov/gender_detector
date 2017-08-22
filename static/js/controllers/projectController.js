myApp.controller("projectController", ['$scope', 'ModalService', '$http', function ($scope, ModalService, $http) {
    $scope.createNewFlag = false;

    $scope.allProjects = null;

    $scope.projectObject = {
        title: null,
        description: null
    };

    $scope.createNewFormFunc = function () {
        $scope.createNewFlag = !$scope.createNewFlag;
    };

    $scope.deleteObject = function (item) {
        item.object_type = "project";
        $http({
            method: 'POST',
            dataType: 'json',
            url: urlsList.project.delete,
            data: JSON.stringify(item),
            contentType: 'application/json'
        }).then(function successCallback(response) {
            $scope.loadAllProjects();
        }, function errorCallback(response) {
        })
    };

    $scope.createProjectFunc = function () {
        $http({
            method: 'POST',
            dataType: 'json',
            url: urlsList.project.create,
            data: JSON.stringify($scope.projectObject),
            contentType: 'application/json'
        }).then(function successCallback(response) {
            $scope.loadAllProjects();
        }, function errorCallback(response) {
        })
    };

    $scope.loadAllProjects = function () {
        $http({
            method: 'GET',
            url: urlsList.project.load_all
        }).then(function successCallback(response) {
            $scope.allProjects = response.data;
        }, function errorCallback(response) {
        });
    };

    $scope.loadAllProjects();

    $scope.checked = false;
    $scope.size = '100px';

    $scope.toggle = function (item) {
        $scope.selectedItem = item;
        $scope.checked = !$scope.checked;
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
    };
}]);