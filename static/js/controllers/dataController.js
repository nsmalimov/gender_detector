myApp.controller("dataController", ['$scope', 'ModalService', '$http', function ($scope, ModalService, $http) {
    $scope.allProjects = null;

    $scope.allRecords = null;

    $scope.selectedProject = null;

    $scope.allRecordsByProjectId = null;

    $scope.project_id = null;

    $scope.file = null;

    $scope.readFile = function (event) {
        var files = event.files;
        var fd = new FormData();
        fd.append("file", files[0]);

        $scope.file = fd;
    };

    $scope.uploadFile = function () {
        $http.post(baseUrl + urlsList.data.upload_one + "/" + $scope.project_id, $scope.file, {
            withCredentials: true,
            headers: {'Content-Type': undefined},
            transformRequest: angular.identity
        }).then(function (response) {
                $scope.loadAllDataByProjectId($scope.project_id);
                document.getElementById('file-input').value = null;
            },
            function (response) {
            });
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

    $scope.loadAllData = function () {
        $http({
            method: 'GET',
            url: urlsList.data.load_all
        }).then(function successCallback(response) {
            $scope.allRecords = response.data;
            //alert($scope.allProjects);
        }, function errorCallback(response) {
        });
    };

    $scope.loadAllDataByProjectId = function (project_id) {
        $http({
            method: 'POST',
            dataType: 'json',
            url: urlsList.data.load_all_by_project,
            data: JSON.stringify({project_id: project_id}),
            contentType: 'application/json'
        }).then(function successCallback(response) {
            $scope.allRecordsByProjectId = response.data;
        }, function errorCallback(response) {
        })
    };

    $scope.loadAllProjects();

    $scope.onSelectUiClick = function (project_id) {
        $scope.project_id = project_id;
        $scope.loadAllDataByProjectId(project_id);
    };

    $scope.showDescriptionModal = function () {
        ModalService.showModal({
            templateUrl: "/static/partials/modals/dataDesc.html",
            controller: "modalController"
        }).then(function (modal) {
            modal.element.modal();
            modal.close.then(function () {
            });
        });
    };

    $scope.deleteObject = function(item) {
        item.object_type = "data";
        $http({
            method: 'POST',
            dataType: 'json',
            url: urlsList.data.delete,
            data: JSON.stringify(item),
            contentType: 'application/json'
        }).then(function successCallback(response) {
            $scope.loadAllDataByProjectId(item.project_id);
            $scope.toggle();
        }, function errorCallback(response) {
        })
    };

    $scope.checked = false;
    $scope.size = '100px';

    $scope.toggle = function (item) {
        $scope.selectedItem = item;
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
    };
}]);