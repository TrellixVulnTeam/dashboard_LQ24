var app = angular.module('stats', []);

app.controller('buildsController', ['buildsRetriever', function(buildsRetriever) {
    buildsRetriever.refresh(this);
 //   this.count = buildsRetriever.total_count;
 }]);

app.controller('bugsController', ['bugsRetriever', function(bugsRetriever) {
    bugsRetriever.refresh(this);
 //   this.count = bugsRetriever.total_count;
 }]);
