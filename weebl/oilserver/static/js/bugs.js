var app = angular.module('stats', ['ngRoute']);

app.controller('bugsController', ['bugsRetriever', function(bugsRetriever) {
    bugsRetriever.refresh(this);
 //   this.count = bugsRetriever.total_count;
 }]);
