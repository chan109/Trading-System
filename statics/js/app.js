var myapp = angular.module("warren", []);
var host = "http://localhost:5000/stocks/all";

myapp.controller("mainController", function ($scope, $http) {

    //sample data
    //$scope.stocks = [{"name": "Fincad", "number": 5}, {"name": "Microsoft", "number": 4}, {"name": "Google", "number": 3},
    //                {"name": "AppNeta", "number": 5}];

    //start polling data from the service

    $http({
        url: host,
        method: "GET"
    }).then(function successCallback(response) {
        debugger;
        console.log(response.data);
        $scope.stocks=response.data;
        // this callback will be called asynchronously
        // when the response is available
    }, function errorCallback(response) {
        console.log(response);
        // called asynchronously if an error occurs
        // or server returns response with an error status.
    });
});
