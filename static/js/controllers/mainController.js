myApp.controller("mainController", function ($scope) {
}).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});