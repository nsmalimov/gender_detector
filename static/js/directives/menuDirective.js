myApp
    .directive('toggleClass', function () {
        return {
            restrict: 'A',
            scope: true,
            template: '<a style="margin-top: 8px;" href="" class="btn btn-default" id="menu-toggle" ng-click="click()">Menu</a>',
            controller: function ($scope, $element) {
                $scope.clicked = 0;
                $scope.click = function () {
                    $scope.clicked++;
                    var elem = angular.element(document.querySelector('#wrapper'));
                    angular.element(elem).toggleClass("toggled");
                }
            }
        }
    });
