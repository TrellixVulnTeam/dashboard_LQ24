app.factory('graphFactory', ['Common', function(Common) {

var calcPercentage = function calcPercentage(value, total, number_of_tests_skipped) {
    if (angular.isUndefined(number_of_tests_skipped))  number_of_tests_skipped = 0;
    total = total - number_of_tests_skipped;
    var percentage = d3.format(',.2f')(((value / total) * 100))
    if (percentage == "NaN"){
        return "0";
    } else {
        return percentage;
    }
};

var plot_stats_graph = function(scope, graphValues, jobDetails) {

    function updateChartData(graphValues, stack_bar_data) {
        var stack_bar_config = {
            visible: true,
            extended: false,
            disabled: false,
            autorefresh: true,
            refreshDataOnly: false,
            debounce: 10
        };
        scope.stack_bar_config = stack_bar_config;

        var individual_stack_bar_options = {
            chart: {
                type: 'discreteBarChart',
                height: 450,
                x: function(d){return d.label;},
                y: function(d){return d.individualPercentage;},
                showValues: true,
                valueFormat: function(d){return d + "%";},
                transitionDuration: 500,
                xAxis: {
                    axisLabel: 'Job Name'
                },
                yAxis: {
                    axisLabel: 'Percentage Success Rate',
                    tickFormat: function(d) {
                        return d3.format(',d')(d);
                    }
                },
                yDomain: [0, 100]
            },
            title: {
                enable: true,
                text: "Percentage Success Rates for " + graphValues.total.meta.total_count + " Matching Tests in " + graphValues.pipeline_total.meta.total_count + " Test Runs",
                css: {
                    textAlign: "center"
                }
            }
        };
        scope.individual_stack_bar_options = individual_stack_bar_options;
        scope.stack_bar_data = stack_bar_data;
    };

    var vals = new Array(Object.keys(jobDetails).length);
    angular.forEach(jobDetails, function(job_info){
        job = job_info.name;
        if (angular.isDefined(graphValues[job])) {
            vals.push({
                "label" : jobDetails[job].description,
                "value" : graphValues[job].pass.meta.total_count,
                "individualPercentage" : calcPercentage(
                    graphValues[job].pass.meta.total_count,
                    graphValues[job].jobtotal.meta.total_count,
                    graphValues[job].skip.meta.total_count),
                "color" : '#' + jobDetails[job].colour
            });
        };
    });
    var stack_bar_data = [{
        key: "Test Run Success",
        values: vals.filter(function(n){ return n != undefined })
    }];

    updateChartData(graphValues, stack_bar_data);

};

var plotBugHistoryGraph = function(scope, graphValues) {
    function updateBugChartData(title, subtitle, bugnumber, description, values, maxNum, minDate) {
        var LineChart_config = {
            visible: true,
            extended: false,
            disabled: false,
            autorefresh: true,
            refreshDataOnly: false,
            debounce: 10
        };
        scope.LineChart_config = LineChart_config;

        var LineChart_options = {
            chart: {
                type: 'lineChart',
                height: 450,
                margin : {
                    top: 20,
                    right: 20,
                    bottom: 40,
                    left: 55
                },
                x: function(d){ return new Date(d.date).getTime(); },
                y: function(d){ return d.count; },
                useInteractiveGuideline: true,
                dispatch: {
                    stateChange: function(e){ console.log("stateChange"); },
                    changeState: function(e){ console.log("changeState"); },
                    tooltipShow: function(e){ console.log("tooltipShow"); },
                    tooltipHide: function(e){ console.log("tooltipHide"); }
                },
                xAxis: {
                    axisLabel: 'Date',
                    tickFormat: function(d) {
                        return d3.time.format('%d-%B-%y')(new Date(d))
                    },
                    showMaxMin: false,
                    staggerLabels: false
                },
                yAxis: {
                    axisLabel: 'Number of Occurrences',
                    axisLabelDistance: -10
                },
                xDomain: [minDate, new Date().getTime()],
                yDomain: [0, maxNum],
                callback: function(chart){
                    console.log("Plotting " + title);
                }
            },
            title: {
                enable: true,
                text: title,
                css: {
                    'font-weight': 'bold'
                }
            },
            subtitle: {
                enable: true,
                text: subtitle,
                css: {
                    'text-align': 'center',
                    'margin': '10px 13px 0px 7px',
                    'font-size': '75%'
                }
            }
        };
        scope.LineChart_options = LineChart_options;

        var LineChart_data = [
            {
                key: "Bug #" + bugnumber,
                values: values,
                area: true,
                color: "#411934"
            }
        ];
        scope.LineChart_data = LineChart_data;
    };

    updateBugChartData(
        graphValues.title,
        graphValues.subtitle,
        graphValues.bugnumber,
        graphValues.description,
        graphValues.data,
        graphValues.maxNum + 5,
        graphValues.minDate
    )
  };

  return {
    plot_stats_graph: plot_stats_graph,
    plotBugHistoryGraph: plotBugHistoryGraph,
    calcPercentage: calcPercentage
  };
}]);
