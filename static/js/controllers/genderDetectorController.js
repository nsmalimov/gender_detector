myApp.controller("genderDetectorController", ['$scope', '$http', function ($scope, $http) {

    $scope.fullProbaMale = null;
    $scope.fullProbaFemale = null;

    $scope.gotProbasFromServerMale = null;
    $scope.gotProbasFromServerFemale = null;

    $scope.probasMaleArr = [];
    $scope.probasFemaleArr = [];

    $scope.isUsed = false;

    $scope.historyText = "";

    $scope.textFromInput = null;

    $scope.init = function () {
    };

    $scope.resetData = function () {
        $scope.textFromInput = null;
    };

    $scope.getGender = function () {
        $scope.getProbasFromServer({"text": $scope.textFromInput});
        $scope.isUsed = true;
    };

    $scope.resetHistory = function () {
        $scope.resetData();
        $scope.historyText = "";
        $scope.isUsed = false;
    };

    $scope.init();

    $scope.getMeanInArray = function (array) {
        var total = 0;
        for (var i = 0; i < array.length; i++) {
            total += array[i];
        }
        return total / array.length;
    };

    $scope.getProbasFromServer = function (item) {
        console.log(JSON.stringify(item));
        $http({
            method: 'POST',
            dataType: 'json',
            url: urlsList.ml_processing.get_probas,
            data: JSON.stringify(item),
            contentType: 'application/json'
        }).then(function successCallback(response) {
            var data = response.data;
            $scope.gotProbasFromServerMale = response.data.proba_male + "%";
            $scope.gotProbasFromServerFemale = response.data.proba_female + "%";

            $scope.probasMaleArr.push(parseInt(response.data.proba_male));
            $scope.probasFemaleArr.push(parseInt(response.data.proba_female));

            $scope.fullProbaMale = $scope.getMeanInArray($scope.probasMaleArr) + "%";
            $scope.fullProbaFemale = $scope.getMeanInArray($scope.probasFemaleArr) + "%";

            $scope.historyText += $scope.textFromInput + " m:" + $scope.gotProbasFromServerMale  + " f:"
                + $scope.gotProbasFromServerFemale + "<br>";

            $scope.resetData();
        }, function errorCallback(response) {
        })
    };
}]);