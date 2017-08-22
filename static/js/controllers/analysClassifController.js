myApp.controller("analysClassifController", function ($scope, $http) {

    $scope.selectedObjects = {
        "selectedProject": null,
        "selectedRecord": null,
        "selectedAlgorithm": null,
        "selectedResultType": null
    };

    $scope.selectType = null;

    $scope.selectedProject = null;
    $scope.selectedRecord = null;
    $scope.selectedAlgorithm = null;
    $scope.selectedResultType = null;

    $scope.type = null;
    $scope.metrics = null;
    $scope.resultImages = null;

    // TODO выбор нескольких алгоритмов
    $scope.selectedAlgorithmsArray = [];

    $scope.commonAlgorithms = null;

    $scope.algorithmsByProjectAndCommon = null;

    $scope.resultTypes = null;

    $scope.loadAllProjects = function () {
        $http({
            method: 'GET',
            url: urlsList.project.load_all
        }).then(function successCallback(response) {
            $scope.allProjects = response.data;
        }, function errorCallback(response) {
        });
    };

    $scope.concatAlgorithmsTypes = function () {
        $scope.algorithmsByProjectAndCommon = $scope.allAlgorithmsByProjectId.concat($scope.commonAlgorithms);
    };

    $scope.loadAllProjects();

    $scope.loadAllDataByProjectId = function (project_id) {
        if (project_id) {
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
        }
    };

    $scope.loadAllAlgorithmsByProjectId = function (project_id) {
        if (project_id) {
            $http({
                method: 'POST',
                dataType: 'json',
                url: urlsList.algorithm.load_all_by_project,
                data: JSON.stringify({project_id: project_id}),
                contentType: 'application/json'
            }).then(function successCallback(response) {
                $scope.allAlgorithmsByProjectId = response.data;
                $scope.concatAlgorithmsTypes();
            }, function errorCallback(response) {
            })
        }
    };

    $scope.startProcessing = function (selectedObjects) {
        $http({
            method: 'POST',
            dataType: 'json',
            url: urlsList.analysClassif.start_processing,
            data: JSON.stringify({
                "selectedProject": selectedObjects.selectedProject.id,
                "selectedRecord": selectedObjects.selectedRecord.id,
                "selectedAlgorithm": selectedObjects.selectedAlgorithm.id,
                "selectedResultType": selectedObjects.selectedResultType.id
            }),
            contentType: 'application/json'
        }).then(function successCallback(response) {
            var dataProcessingResult = response.data;
            console.log(dataProcessingResult);
            $scope.type = dataProcessingResult['type'];

            switch ($scope.type) {
                case "train_save_metrics_graphics":
                    $scope.metrics = dataProcessingResult['metrics'];
                    $scope.img = dataProcessingResult['img'];
                    break;
                default:
                    break;
            }
        }, function errorCallback(response) {
        })
    };

    $scope.loadAllCommonAlgorithms = function (project_id) {
        $http({
            method: 'GET',
            url: urlsList.algorithm.load_all_common
        }).then(function successCallback(response) {
            $scope.commonAlgorithms = response.data;
        }, function errorCallback(response) {
        });
    };

    $scope.loadAllAnalysClassifByProjectId = function (project_id) {
        if (project_id) {

        }
    };

    $scope.loadAllResultTypes = function () {
        $http({
            method: 'GET',
            url: urlsList.analysClassif.load_all_result_types
        }).then(function successCallback(response) {
            $scope.resultTypes = response.data;
        }, function errorCallback(response) {
        });
    };

    $scope.changeColor = function (styleVar) {
        $scope[styleVar]={color:'blue'};
    };

    $scope.loadAllCommonAlgorithms();

    $scope.loadAllResultTypes();
});