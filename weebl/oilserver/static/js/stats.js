var app = angular.module('weebl');
app.controller('successRateController', [
    '$scope', '$rootScope', 'buildsRetriever', 'bugsRetriever', 'SearchService', 'metadataRetriever', 'DataService',
    function($scope, $rootScope, buildsRetriever, bugsRetriever, SearchService, metadataRetriever, DataService) {
        binding = this;
        binding.user = $scope.this.user;
        binding.apikey = $scope.this.apikey;
        $scope.filters = SearchService.getEmptyFilter();
        $scope.bugs = {};
        $scope.testRuns = {};
        $scope.metadata = {};
        $scope.regexes = {};

        $scope.tabs = {};

        $scope.tabs.successRate = {};
        $scope.tabs.successRate.pagetitle = "Success Rate";
        $scope.tabs.successRate.currentpage = "successRate";

        $scope.tabs.bugs = {};
        $scope.tabs.bugs.pagetitle = "Bugs";
        $scope.tabs.bugs.currentpage = "bugs";
        $scope.tabs.bugs.predicate = "occurrences";
        $scope.tabs.bugs.reverse = false;

        $scope.tabs.testRuns = {};
        $scope.tabs.testRuns.pagetitle = "Test Runs";
        $scope.tabs.testRuns.currentpage = "testRuns";
        $scope.tabs.testRuns.predicate = "completed_at";
        $scope.tabs.testRuns.reverse = false;

        $scope.tabs.individual_testRun = {};
        $scope.tabs.individual_testRun.pagetitle = "Individual Test Run";
        $scope.tabs.individual_testRun.currentpage = "individual_testRun";

        function generatePipelineFilters() {
            var pipeline_filters = {};

            if ($scope.start_date)
                pipeline_filters['completed_at__gte'] = $scope.start_date;
            if ($scope.finish_date)
                pipeline_filters['completed_at__lte'] = $scope.finish_date;

            for (var enum_field in $scope.filters) {
                if (!(enum_field in $scope.metadata))
                    continue;

                enum_values = [];
                $scope.filters[enum_field].forEach(function(enum_value) {
                    enum_values.push(enum_value.substr(1));
                });

                /*
                 * Unlike other filter fields, environment is a few relations
                 * away and so we need to explicitly build its filter.
                 */
                if (enum_field == 'environment') {
                    api_enum_name = 'buildexecutor__jenkins__environment';
                } else {
                    api_enum_name = metadataRetriever.enum_fields[enum_field];
                }

                pipeline_filters[api_enum_name + '__name__in'] = enum_values;
            }

            return pipeline_filters;
        }

        function updateStats(pipeline_filters) {
            buildsRetriever.refresh(binding, pipeline_filters);
        };

        function updateBugs(pipeline_filters) {
            bugsRetriever.refresh($scope, pipeline_filters);
        };

        function updateRegexes(pipeline_filters) {
            $scope.regexes = DataService.refresh(
                'knownbugregex', $scope.user, $scope.apikey).get(pipeline_filters);
        };

        function updateTestRuns(pipeline_filters) {
            $scope.testRuns = DataService.refresh(
                'pipeline', $scope.user, $scope.apikey).get(pipeline_filters);
        };

        function dateToString(date) {
            return date.getUTCFullYear() + "-" + (date.getUTCMonth() + 1) + "-" + date.getUTCDate();
        }

        $scope.humaniseDate = function(datestr) {
            var date_obj = new Date(datestr);
            var monthNames = ["Jan", "Feb", "Mar","Apr", "May", "Jun",
                              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
            var day = ('0' + date_obj.getUTCDate()).slice(-2);
            var month_name = monthNames[date_obj.getUTCMonth()];
            var year = ('0' + date_obj.getUTCFullYear()).slice(-2);
            var hours = ('0' + date_obj.getUTCHours()).slice(-2);
            var minutes = ('0' + date_obj.getUTCMinutes()).slice(-2);
            var seconds = ('0' + date_obj.getUTCSeconds()).slice(-2);
            return (day + "-" + month_name + "-" + year + " at " + hours + ":" + minutes + ":" + seconds);
        };

        var dateSymbolToDays = {
            'Last 24 Hours': 1,
            'Last 7 Days': 7,
            'Last 30 Days': 30,
            'Last Year': 365
        };

        function updateDates(value) {
            var days_offset = dateSymbolToDays[value];
            console.log("Updating to last %d days.", days_offset);
            today = new Date();
            prior_date = new Date(new Date().setDate(today.getDate()-days_offset));
            $scope.start_date = prior_date.toISOString();
            $scope.finish_date = today.toISOString();
        };

        function updateFromServer() {
            pipeline_filters = generatePipelineFilters();
            updateStats(pipeline_filters);
            updateBugs(pipeline_filters);
            updateTestRuns(pipeline_filters);
        }

        // Clear the search bar.
        $scope.clearSearch = function() {
            $scope.search = "";
            $scope.start_date = null;
            $scope.finish_date = null;
            $scope.updateSearch();
        };

        // Update the filters object when the search bar is updated.
        $scope.updateSearch = function() {
            var filters = SearchService.getCurrentFilters(
                $scope.search);
            if(filters === null) {
                $scope.filters = SearchService.getEmptyFilter();
                $scope.searchValid = false;
            } else {
                $scope.filters = filters;
                $scope.searchValid = true;
            }
            updateFromServer();
        };

        $scope.updateIndividualTestRun = function(pipeline) {
            $scope.individual_testRun = DataService.refresh(
                'pipeline', $scope.user, $scope.apikey).get({"uuid": pipeline});
        };

        $scope.abbreviateUUID = function(UUID) {
            return UUID.slice(0, 4) + "..." + UUID.slice(-5);
        };


        $scope.updateFilter = function(type, value, tab) {
            console.log("Updating filter! %s %s %s", type, value, tab);

            if (type == "date") {
                // Only one date can be set at a time.
                new_value = "=" + value;
                if ($scope.filters["date"] && $scope.filters["date"][0] == new_value) {
                    $scope.filters["date"] = [];
                    $scope.start_date = null;
                    $scope.finish_date = null;
                } else {
                    updateDates(value);
                    $scope.filters["date"] = [new_value];
                }
            } else {
                $scope.filters = SearchService.toggleFilter(
                    $scope.filters, type, value, true);
            }
            $scope.search = SearchService.filtersToString($scope.filters);
            updateFromServer();
        };

        $scope.isFilterActive = function(type, value, tab) {
            return SearchService.isFilterActive(
                $scope.filters, type, value, true);
        };

        // Toggles between the current tab.
        $scope.toggleTab = function(tab) {
            updateFromServer(); // FIXME: Temporary hack. Need to refresh plot rather than redownloading data.
            $rootScope.title = $scope.tabs[tab].pagetitle;
            $scope.currentpage = tab;
        };

        // Sorts the table by predicate.
        $scope.sortTable = function(predicate, tab) {
            $scope.tabs[tab].predicate = predicate;
            $scope.tabs[tab].reverse = !$scope.tabs[tab].reverse;
        };

        metadataRetriever.refresh($scope);
        $scope.updateFilter('date', 'Last 24 Hours', 'successRate');
        $scope.toggleTab('successRate');
        $scope.sortTable('occurrence_count', 'bugs');
    }]);
