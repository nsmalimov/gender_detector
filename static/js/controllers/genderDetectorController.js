myApp.controller("genderDetectorController", ['$scope', 'ModalService', '$http', function ($scope, ModalService, $http) {

    $scope.fullProbaMale = null;
    $scope.fullProbaFemale = null;

    $scope.gotProbasFromServerMale = null;
    $scope.gotProbasFromServerFemale = null;

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
        $scope.isUsed = true;
        $scope.getProbasFromServer({"text": $scope.textFromInput});
    };

    $scope.resetHistory = function () {
        $scope.resetData();
        $scope.historyText = "";
    };

    $scope.init();

    $scope.getProbasFromServer = function (item) {
        $http({
            method: 'POST',
            dataType: 'json',
            url: urlsList.ml_processing.get_probas,
            data: JSON.stringify(item),
            contentType: 'application/json'
        }).then(function successCallback(response) {
            var data = response.data;
            $scope.gotProbasFromServerMale = data.proba_male + "%";
            $scope.gotProbasFromServerFemale = data.proba_female + "%";

        }, function errorCallback(response) {
        })
    };
}]);