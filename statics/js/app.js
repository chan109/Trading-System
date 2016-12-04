var myapp = angular.module("warren", ["zingchart-angularjs"]);
var host = "http://gabrieluribe.me:5000/stocks/all";
var buyHost = "http://gabrieluribe.me:5000/stocks/buy";
var testHost = "http://localhost:5000/stocks/";
var test = "http://localhost:5000/stocks/all";
myapp.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';
}]);

myapp.controller("mainController", function ($scope, $http, $interval) {

    //sample data
    //$scope.stocks = [{"symbol": "Fincad", "price": 5}, {"sybmol": "Microsoft", "price": 4}, {"sybmol": "Google", "price": 3},
    //                {"sybmol": "AppNeta", "price": 5}];

    //start polling data from the service
    $scope.myData = [1,2,28,4,5];


    $http({
        url: test,
        method: "GET"
    }).then(function successCallback(response) {
        console.log(response.data);
        $scope.stocks=response.data;
        // this callbalsck will be called asynchronously
        // when the response is available
    }, function errorCallback(response) {
        console.log(response);
        // called asynchronously if an error occurs
        // or server returns response with an error status.
    });
    
    $scope.buy = function (symbol) {
        debugger;
        $http({
            url: buyHost,
            method: "POST",
            data:"symbol="+symbol
        }).then(function successCallback(response) {
            console.log(response.data);
            debugger
                $scope.stocks=response.data;
            // this callbalsck will be called asynchronously
            // when the response is available
        }, function errorCallback(response) {
            console.log(response);
            // called asynchronously if an error occurs
            // or server returns response with an error status.
        });
    }
});
