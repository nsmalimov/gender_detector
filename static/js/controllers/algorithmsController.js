myApp.controller("algorithmsController", ['$scope', 'ModalService', '$http', function ($scope, ModalService, $http) {
    $scope.allProjects = null;

    $scope.allAlgorithms = null;

    $scope.selectedAlgorithm = null;

    $scope.allAlgorithmsByProjectId = null;

    $scope.project_id = null;

    $scope.fd = new FormData();

    $scope.commonAlgorithmsFlag = false;

    $scope.commonAlgorithms = null;

    $scope.commonAlgorithmsTitles = [];

    $scope.selectedCommonAlgorithmTitle = null;

    $scope.strButtonCheckCommonAlgorithmsFlag = "Показать стандартные";

    $scope.selectedCommonAlgorithm = null;

    $scope.projectObject = {
        title: null,
        description: null
    };

    $scope.readFile = function (event) {
        var files = event.files;
        $scope.fd.append("file", files[0]);
    };

    $scope.uploadFile = function () {
        $scope.fd.append("title", $scope.projectObject.title);
        $scope.fd.append("description", $scope.projectObject.description);

        $http.post(baseUrl + urlsList.algorithm.upload_one + "/" + $scope.project_id, $scope.fd, {
            withCredentials: true,
            headers: {'Content-Type': undefined},
            transformRequest: angular.identity
        }).then(function (response) {
                $scope.loadAllAlgorithmsByProjectId($scope.project_id);
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

    $scope.loadAllAlgorithmsByProjectId = function (project_id) {
        $http({
            method: 'POST',
            dataType: 'json',
            url: urlsList.algorithm.load_all_by_project,
            data: JSON.stringify({project_id: project_id}),
            contentType: 'application/json'
        }).then(function successCallback(response) {
            $scope.allAlgorithmsByProjectId = response.data;
        }, function errorCallback(response) {
        })
    };

    $scope.loadAllCommonAlgorithms = function (project_id) {
        $http({
            method: 'GET',
            url: urlsList.algorithm.load_all_common
        }).then(function successCallback(response) {
            $scope.commonAlgorithms = response.data;

            for (var i in $scope.commonAlgorithms) {
                $scope.commonAlgorithmsTitles.push($scope.commonAlgorithms[i].title + "    ");
            }

            $scope.selectedCommonAlgorithmTitle = $scope.commonAlgorithmsTitles[0];

            $scope.selectedCommonAlgorithm = $scope.commonAlgorithms[0];

        }, function errorCallback(response) {
        });
    };

    $scope.loadAllProjects();

    $scope.loadAllCommonAlgorithms();

    $scope.onSelectUiClick = function (project_id) {
        $scope.project_id = project_id;
        $scope.loadAllAlgorithmsByProjectId(project_id);
    };

    $scope.showDescriptionModal = function () {
        ModalService.showModal({
            templateUrl: "/static/partials/modals/algorithmDesc.html",
            controller: "modalController"
        }).then(function (modal) {
            modal.element.modal();
            modal.close.then(function () {
            });
        });
    };

    $scope.deleteObject = function (item) {
        item.object_type = "algorithm";
        $http({
            method: 'POST',
            dataType: 'json',
            url: urlsList.algorithm.delete,
            data: JSON.stringify(item),
            contentType: 'application/json'
        }).then(function successCallback(response) {
            $scope.loadAllAlgorithmsByProjectId(item.project_id);
            $scope.toggle();
        }, function errorCallback(response) {
        })
    };

    $scope.showCommonAlgorithms = function () {
        $scope.commonAlgorithmsFlag = !$scope.commonAlgorithmsFlag;
        $scope.strButtonCheckCommonAlgorithmsFlag = "Выбрать проект";
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

    $scope.changeCommonAlgorithms = function (selectedCommonAlgorithmTitle) {
        for (var i in $scope.commonAlgorithms) {
            if (selectedCommonAlgorithmTitle === ($scope.commonAlgorithms[i].title + "    ")) {
                $scope.selectedCommonAlgorithm = $scope.commonAlgorithms[i];
            }
        }
    };
}]);