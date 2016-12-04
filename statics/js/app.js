var myapp = angular.module("warren", ["zingchart-angularjs"]);
var host = "http://gabrieluribe.me:5000/stocks/all";
var test = "http://localhost:5000/stocks/all";

myapp.controller("mainController", function ($scope, $http) {

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
        // this callback will be called asynchronously
        // when the response is available
    }, function errorCallback(response) {
        console.log(response);
        // called asynchronously if an error occurs
        // or server returns response with an error status.
    });
    
    $scope.buy = function (symbol) {
        $http.post("host",symbol).success(function (response) {
            console.log(response);
        })
    }
});
