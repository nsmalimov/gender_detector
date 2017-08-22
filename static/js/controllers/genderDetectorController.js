myApp.controller("genderDetectorController", ['$scope', 'ModalService', '$http', function ($scope, ModalService, $http) {

    $scope.fullProbaMale = null;
    $scope.fullProbaFemale = null;

    $scope.isUsed = false;

    $scope.historyText = "";

    $scope.textFromInput = null;

    $scope.init = function () {
    };

    $scope.resetData = function () {
        $scope.textFromInput = null;
    };

    $scope.getGender = function () {
        $scope.historyText += $scope.textFromInput + "<br>";
        $scope.resetData();
    };

    $scope.resetHistory = function () {
        $scope.resetData();
        $scope.historyText = "";
    };

    $scope.init();
}]);