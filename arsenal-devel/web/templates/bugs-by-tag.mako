<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<%
    importance_color = {
            "Unknown"       : "importance-unknown",
            "Critical"      : "importance-critical",
            "High"          : "importance-high",
            "Medium"        : "importance-medium",
            "Low"           : "importance-low",
            "Wishlist"      : "importance-wishlist",
            "Undecided"     : "importance-undecided"
        }
    status_color     = {
            "New"           : "status-new",
            "Incomplete"    : "status-incomplete",
            "Confirmed"     : "status-confirmed",
            "Triaged"       : "status-triaged",
            "In Progress"   : "status-in_progress",
            "Fix Committed" : "status-fix_committed",
            "Fix Released"  : "status-fix_released",
            "Invalid"       : "status-invalid",
            "Won't Fix"     : "status-wont_fix",
            "Opinion"       : "status-opinion",
            "Expired"       : "status-expired",
            "Unknown"       : "status-unknown"
        }
        
    bugs_by_tag = {}
    tasks = template_data['tasks']
    tags = {}
    for bug in tasks:
        bug_tags = tasks[bug][0]['bug']['tags']
        tags[bug] = ['untagged'] if bug_tags == [] else bug_tags

    for bid in tasks:
        for t in tasks[bid]:
            for tag in tags[bid]:
                if tag not in bugs_by_tag:
                    bugs_by_tag[tag] = {}

                if bid not in bugs_by_tag[tag]:
                    bugs_by_tag[tag][bid] = []

                if t['bug']['tags'] not in bugs_by_tag[tag][bid]:
                    bugs_by_tag[tag][bid].append(t['bug']['tags'])


    tag_report_order = []
    if 'untagged' in bugs_by_tag:
        tag_report_order.append('untagged') # We want untagged first
    for t in sorted(bugs_by_tag):
        if t != 'untagged':
            tag_report_order.append(t)
    report_options = template_data['report']

    LP_link = template_data['launchpad_config'].get('launchpad_link')
    LP_link += "/+bugs?field.{0}={1}"
%>
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="en-US">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<title>${report_title}</title>

        <link title="light" rel="stylesheet" href="http://people.canonical.com/~kernel/reports/css/light-style.css" type="text/css" media="print, projection, screen" />
        <link title="dark"  rel="stylesheet" href="http://people.canonical.com/~kernel/reports/css/dark-style.css"  type="text/css" media="print, projection, screen" />

        <script type="text/javascript" src="http://people.canonical.com/~kernel/reports/js/styleswitcher.js"></script>

        <link href='http://fonts.googleapis.com/css?family=Cantarell&subset=latin' rel='stylesheet' type='text/css'>
        <script type="text/javascript" src="http://people.canonical.com/~kernel/reports/js/jquery-latest.js"></script>
        <script type="text/javascript" src="http://people.canonical.com/~kernel/reports/js/jquery.tablesorter.js"></script>

    </head>

    <body class="bugbody">
        <!-- Top Panel -->
        <div id="toppanel">
            <!-- Sliding Panel
            -->
            <div id="panel">
                <form name="filter">
                <div class="content clearfix" style="height:250px; overflow:auto;">
                    <table width="100%">
                        <tr valign="top">
                            <td valign="top" width="15%">
                                <input type="button" class="l2-section-heading" onclick="checkAll(this, 'importance')" value="Importance (Click to toggle)"/>
                                <table width="100%">
                                    <tr><td width="50%"> <input type="checkbox" name="importance" onclick="importance_handler(this, 'importance', true)" checked value="Critical"  /> <a href="${LP_link.format('importance', 'CRITICAL')}">    Critical    </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="importance" onclick="importance_handler(this, 'importance', true)" checked value="Low"       /> <a href="${LP_link.format('importance', 'LOW')}">         Low         </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="importance" onclick="importance_handler(this, 'importance', true)" checked value="High"      /> <a href="${LP_link.format('importance', 'HIGH')}">        High        </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="importance" onclick="importance_handler(this, 'importance', true)" checked value="Wishlist"  /> <a href="${LP_link.format('importance', 'WISHLIST')}">    Wishlist    </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="importance" onclick="importance_handler(this, 'importance', true)" checked value="Medium"    /> <a href="${LP_link.format('importance', 'MEDIUM')}">      Medium      </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="importance" onclick="importance_handler(this, 'importance', true)" checked value="Undecided" /> <a href="${LP_link.format('importance', 'UNDECIDED')}">   Undecided   </a> </td></tr>
                                </table>
                            </td>

                            <td width="20">&nbsp;</td>

                            <td valign="top">
                                <input type="button" class="l2-section-heading" onclick="checkAll(this, 'status')" value="Status (Click to toggle)"/>
                                <table width="100%">
                                    <tr><td width="50%"> <input type="checkbox" name="status" onclick="status_handler(this, 'status', true)" checked value="New"           /> <a href="${LP_link.format('status', 'NEW')}">         New           </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="status" onclick="status_handler(this, 'status', true)" checked value="Incomplete"    /> <a href="${LP_link.format('status', 'INCOMPLETE')}">  Incomplete    </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="status" onclick="status_handler(this, 'status', true)" checked value="Confirmed"     /> <a href="${LP_link.format('status', 'CONFIRMED')}">   Confirmed     </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="status" onclick="status_handler(this, 'status', true)" checked value="Fix Released"  /> <a href="${LP_link.format('status', 'FIXRELEASED')}"> Fix Released  </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="status" onclick="status_handler(this, 'status', true)" checked value="Triaged"       /> <a href="${LP_link.format('status', 'TRIAGED')}">     Triaged       </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="status" onclick="status_handler(this, 'status', true)" checked value="Won't Fix"     /> <a href="${LP_link.format('status', 'WONTFIX')}">     Won't Fix     </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="status" onclick="status_handler(this, 'status', true)" checked value="In Progress"   /> <a href="${LP_link.format('status', 'INPROGRESS')}">  In Progress   </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="status" onclick="status_handler(this, 'status', true)" checked value="Opinion"       /> <a href="${LP_link.format('status', 'OPINION')}">     Opinion       </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="status" onclick="status_handler(this, 'status', true)" checked value="Fix Committed" /> <a href="${LP_link.format('status', 'FIXCOMMITTED')}">Fix Committed </a> </td></tr>
                                    <tr><td width="50%"> <input type="checkbox" name="status" onclick="status_handler(this, 'status', true)" checked value="Invalid"       /> <a href="${LP_link.format('status', 'INVALID')}">     Invalid       </a> </td></tr>
                                </table>
                            </td>

                            <td width="20">&nbsp;</td>

                            <td valign="top" width="65%">
                                <input type="button" class="l2-section-heading" onclick="checkAll(this, 'tag_values')" value="Tags (Click to toggle)"/>
                                <table width="85%">
                                    % for counter, elem in enumerate(tag_report_order):
                                        % if (counter % 3) == 0:
                                            <tr>
                                        % endif
                                            <td width="33%"> <input type="checkbox" name="tag_values" onclick="tag_values_handler(this, 'tag_values', true)" checked value="${elem}"    /> <a href="${LP_link.format('tag', elem) if elem != 'untagged' else 'https://bugs.launchpad.net/launchpad/+bug/347015'}"> ${elem}  </a> </td>
                                        % if (counter == len(tag_report_order)) or ((counter % 3) == 2):
                                            </tr>
                                        % endif
                                    % endfor
                                </table>
                            </td>

                        </tr>

                        <!--
                        <tr valign="top">

                            <td valign="top" width="30%" colspan="5">
                                <p class="l2-section-heading">Assignee</p>
                                <table width="100%">
                                    % for i, elem in enumerate(assignees_list):
                                        % if i % 5 == 0:
                                        <tr>
                                        % endif
                                            <td width="20%"> <input type="checkbox" name="assignees"  onclick="assignee_handler(this, 'series', true)" checked value="${assignees_list[i]}"         /> ${assignees_list[i]} </td>
                                        % if i % 5 == 4:
                                        </tr>
                                        % endif
                                    % endfor
                                </table>
                            </td>
                        </tr>

                        <tr valign="top">

                            <td valign="top">
                                <p class="l2-section-heading">Date</p>
                                <table width="100%">
                                    <tr><td colspan="4">Created within:</td></tr>
                                    <tr><td width="10">&nbsp;</td>
                                        <td width="50"> <input type="radio" name="date"     onclick="date_handler(this, 'date', true)" checked value="1"    /> 24 Hrs.   </td>
                                        <td width="50"> <input type="radio" name="date"     onclick="date_handler(this, 'date', true)" checked value="7"    /> 1 Week    </td>
                                        <td width="50"> <input type="radio" name="date"     onclick="date_handler(this, 'date', true)" checked value="30"   /> 1 Month   </td></tr>
                                    <tr><td width="10">&nbsp;</td>
                                        <td width="50"> <input type="radio" name="date"     onclick="date_handler(this, 'date', true)" checked value="-1"   /> Unlimited </td></tr>
                                </table>
                            </td>

                            <td width="20">&nbsp;</td>

                            <td valign="top">
                                &nbsp;
                            </td>

                            <td width="20">&nbsp;</td>

                            <td valign="top">
                                &nbsp;
                            </td>
                        </tr>
                        -->

                    </table>

                </div>
                </form>

                <div style="clear:both;"></div>
            </div> <!-- panel -->

            <!-- The tab on top -->
            <div class="tab">
                <ul class="login">
                    <li class="left">&nbsp;</li>
                    <li id="toggle">
                        <a id="open" class="open" href="#">&nbsp;Options</a>
                        <a id="close" style="display: none;" class="close" href="#">&nbsp;Close&nbsp;&nbsp;</a>
                    </li>
                    <li class="right">&nbsp;</li>
                </ul>
            </div> <!-- / top -->
        </div> <!-- Top Panel -->

        <div class="outermost">
            <div class="title">
		    ${report_title} 
            </div>
            <div class="section">
                <p><span style="color:red">WARNING: </span>This data was generated at: ${template_data['update_timestamp']} and as such, may not be up to date.</p>
                <hr />
            </div>
            <div class="section">
                % for tag in tag_report_order:
                    <% total = len(bugs_by_tag[tag].keys()) %>
                    <div class="section-heading">${tag}&nbsp;&nbsp;(<span id="${tag}-total">${total}</span>)</div>

                    <% id = tag.replace(' ', '_') %>
                    <table id="${id}" class="tablesorter" border="0" cellpadding="0" cellspacing="1" width="100%%">
                        <thead>
                            <tr>
                                <th width="40">Bug</th>
                                <th>Summary</th>
                                <th width="100">All Tags</th>
                                <th width="80">Importance</th>
                                <th width="80">Status</th>
                                <th width="130">Assignee</th>
                                <th width="130">Owner</th>
                                <th width="100">Created</th>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>
                % endfor

            </div>
            <br />
            <br />
            <div>
                <div id="bug-total">Total number of bugs: 000</div>
                <div id="tag-total">Total number of tags: 000</div>
            </div>
            <div>
                <br />
                <hr />
                <table width="100%%" cellspacing="0" cellpadding="0">
                    <thead>
                        <tr>
                            <td width="100">Column</td>
                            <td>Description</td>
                        </tr>
                    </th>
                    <tbody>
                        <tr><td>Bug       </td><td>The Launchpad Bug number and a link to the Launchpad Bug.            </td></tr>
                        <tr><td>Summary   </td><td>The 'summary' or 'title' from the bug.                               </td></tr>
                        <tr><td>All Tags  </td><td>All tags given to the bug.                                           </td></tr>
                        <tr><td>Importance</td><td>The bug task's importance.                                           </td></tr>
                        <tr><td>Status    </td><td>The bug task's status.                                               </td></tr>
                        <tr><td>Assignee  </td><td>The person or team assigned to work on the bug.                      </td></tr>
                        <tr><td>Owner     </td><td>The person who originally opened the bug.                            </td></tr>
                        <tr><td>Created   </td><td>The date the bug was created the value in parens is age in days.     </td></tr>
                    </tbody>
                </table>
                <br />
            </div>
            <div>
                <br />
                <hr />
                <table width="100%%" cellspacing="0" cellpadding="0">
                    <tr>
                        <td>
                            ${timestamp}
                        </td>
                        <td align="right">
                            &nbsp;
                            Themes:&nbsp;&nbsp;
                            <a href='#' onclick="setActiveStyleSheet('dark'); return false;">DARK</a>
                            &nbsp;
                            <a href='#' onclick="setActiveStyleSheet('light'); return false;">LIGHT</a>
                        </td>
                    </tr>
                </table>
                <br />
            </div>


        </div> <!-- Outermost -->
    </body>

    <script type="text/javascript">
       // add parser through the tablesorter addParser method
       $.tablesorter.addParser({
           // set a unique id
           id: 'age',
           is: function(s) { return false; },
           format: function(s) {
               // format your data for normalization
               fields  = s.split('.')
               days    = parseInt(fields[0], 10) * (60 * 24);
               hours   = parseInt(fields[1], 10) * 60;
               minutes = parseInt(fields[2]);
               total   = minutes + hours + days
               return total;
           },
           // set type, either numeric or text
           type: 'numeric'
       });

       // add parser through the tablesorter addParser method
       $.tablesorter.addParser({
           // set a unique id
           id: 'importance',
           is: function(s) { return false; },
           format: function(s) {
               // format your data for normalization
               return s.toLowerCase().replace(/critical/,6).replace(/high/,5).replace(/medium/,4).replace(/low/,3).replace(/wishlist/,2).replace(/undecided/,1).replace(/unknown/,0);
           },
           // set type, either numeric or text
           type: 'numeric'
       });

       // add parser through the tablesorter addParser method
       $.tablesorter.addParser({
           // set a unique id
           id: 'status',
           is: function(s) { return false;
           },
           format: function(s) {
               // format your data for normalization
               return s.toLowerCase().replace(/new/,12).replace(/incomplete/,11).replace(/confirmed/,10).replace(/triaged/,9).replace(/in progress/,8).replace(/fix committed/,7).replace(/fix released/,6).replace(/invalid/,5).replace(/won't fix/,4).replace(/confirmed/,3).replace(/opinion/,2).replace(/expired/,1).replace(/unknown/,0);
           },
           // set type, either numeric or text
           type: 'numeric'
       });

       $(function() {
            % for tag in tag_report_order:
                <% id = tag.replace(' ', '_') %>
                $("#${id}").tablesorter({
                    headers: {
                        3: {
                            sorter:'importance'
                        },
                        4: {
                            sorter:'status'
                        }
                    },
                    widgets: ['zebra']
                });
            % endfor
        });
    </script>

    <script type="text/javascript">
        var tag_values = [
            % for tag in tag_report_order:
                "${tag}",
            % endfor
            ];
        var importance = ["Critical", "Low", "High", "Wishlist", "Medium", "Undecided"];
        var task_status = ["New", "Incomplete", "Confirmed", "Fix Released", "Triaged", "Won't Fix", "In Progress", "Opinion", "Fix Committed", "Invalid"];
        var assignees = [];
        var date_filter = -1;
        var jd = ${json_data_string};
        var first_time = true;

        var importance_color = {
                "Unknown"       : "importance-unknown",
                "Critical"      : "importance-critical",
                "High"          : "importance-high",
                "Medium"        : "importance-medium",
                "Low"           : "importance-low",
                "Wishlist"      : "importance-wishlist",
                "Undecided"     : "importance-undecided"
            };

        var status_color = {
                "New"           : "status-new",
                "Incomplete"    : "status-incomplete",
                "Confirmed"     : "status-confirmed",
                "Triaged"       : "status-triaged",
                "In Progress"   : "status-in_progress",
                "Fix Committed" : "status-fix_committed",
                "Fix Released"  : "status-fix_released",
                "Invalid"       : "status-invalid",
                "Won't Fix"     : "status-wont_fix",
                "Opinion"       : "status-opinion",
                "Expired"       : "status-expired",
                "Unknown"       : "status-unknown"
            };

        var tags_id_list = [];
        var tags_id_list = [];
        % for tag in tag_report_order:
            <% id = tag.replace(' ', '_') %>
            tags_id_list.push("${id}");
            tags_id_list.push("${tag}");
        % endfor

        function tag_values_handler(chkbx, grp, update_table) {
            tag_values = [];
            for (i = 0; i < document.filter.length; i++) {
                if (document.filter[i].name == "tag_values") {
                    if (document.filter[i].checked) {
                        tag_values.push(document.filter[i].value);
                    }
                }
            }

            if (update_table) {
                update_tables();
            }
        }

        function importance_handler(chkbx, grp, update_table) {
            importance = [];
            for (i = 0; i < document.filter.length; i++) {
                if (document.filter[i].name == "importance") {
                    if (document.filter[i].checked) {
                        importance.push(document.filter[i].value);
                    }
                }
            }

            if (update_table) {
                update_tables();
            }
        }

        function assignee_handler(chkbx, grp, update_table) {
            assignees = [];
            for (i = 0; i < document.filter.length; i++) {
                if (document.filter[i].name == "assignees") {
                    if (document.filter[i].checked) {
                        assignees.push(document.filter[i].value);
                    }
                }
            }

            if (update_table) {
                update_tables();
            }
        }

        function status_handler(chkbx, grp, update_table) {
            task_status = [];
            for (i = 0; i < document.filter.length; i++) {
                if (document.filter[i].name == "status") {
                    if (document.filter[i].checked) {
                        task_status.push(document.filter[i].value);
                    }
                }
            }

            if (update_table) {
                update_tables();
            }
        }

        function date_handler(chkbx, grp, update_table) {
            date_filter = -1;
            for (i = 0; i < document.filter.length; i++) {
                if (document.filter[i].name == "date") {
                    if (document.filter[i].checked) {
                        date_filter = parseInt(document.filter[i].value);
                    }
                }
            }

            if (update_table) {
                update_tables();
            }
        }

        function checkAll(bx, name) {
            var cbs = document.getElementsByTagName('input');
                for(var i=0; i < cbs.length; i++) {
                    if (cbs[i].type == 'checkbox') {
                      if (cbs[i].name == name) {
                          cbs[i].click()
                      }
                    }
                }
            }

        function update_tables() {
            var tag_total = 0;
            var bug_total = 0;
            var tables = {
            % for tag in tag_report_order:
                "${tag}" : "",
            % endfor
            };

            var totals = {
            % for tag in tag_report_order:
                "${tag}" : 0,
            % endfor
            };

            var oddness = {
            % for tag in tag_report_order:
                "${tag}" : true,
            % endfor
            };

            $.each(jd, function(bid, task) {
                var fail = false;
                var last_tbtag_fail = -1;

                $.each(task[0].bug.tags, function(index, tbtag) {
                    if (tag_values.indexOf(tbtag) == -1) {
                        if (last_tbtag_fail == 0) {
                            fail = false;
                            last_tbtag_fail = 0;
                        } else {
                            fail = true
                        }
                    } else {
                        fail = false;
                        last_tbtag_fail = 0;
                    }
                });

                if (!fail && importance.indexOf(task[0].importance) == -1) {
                    fail = true;
                }

                if (!fail && task_status.indexOf(task[0].status) == -1) {
                    fail = true;
                }

                /*
                if (!fail && assignees.indexOf(task[0].assignee) == -1) {
                    fail = true;
                }

                if (!fail && date_filter != -1) {
                    if (task[0].bug.age > date_filter) {
                        fail = true;
                    }
                }
                */

                if (!fail) {
                    bug_total++;
                    s = "";
                    s += "<td><a href=\"http://launchpad.net/bugs/" + bid + "\">" + bid + "</a></td>";
                    s += "<td>" + task[0].bug.title + "</td>";
                    s += "<td>" + task[0].bug.tags + "</td>";
                    s += "<td class=\"" + importance_color[task[0].importance] + "\">" + task[0].importance + "</td>";
                    s += "<td class=\"" + status_color[task[0].status] + "\">" + task[0].status + "</td>";
                    s += "<td>" + task[0].assignee + "</td>";
                    s += "<td>" + task[0].owner + "</td>";
                    s += "<td>" + task[0].bug.iso_date_created + "</td>";
                    s += "</tr>";

                    $.each(task[0].bug.tags, function(index, tbtag) {
                        if (oddness[tbtag]) {
                            s_class = "<tr class=\"odd\">";
                            oddness[tbtag] = false;
                        } else {
                            s_class = "<tr class=\"even\">";
                            oddness[tbtag] = true;
                        }
                        tag_total++;
                        tables[tbtag] += s_class + s;
                        totals[tbtag]++;
                    });
                }
            });


            $.each(tables, function(tag, val) {
                id = tag.replace(/ /g, '_');
                $("#" + id + " tbody").html(tables[tag]);
                $("#" + id).trigger("update");
                document.getElementById(tag + "-total").innerHTML = totals[tag];
            });
            if (first_time) {
                first_time = false;
                sortList = [[3,1], [4,1]];
                $.each(tables, function(tag, val) {
                    id = tag.replace(/ /g, '_');
                    $("#" + id).trigger("sorton", [sortList]);
                });
            }
            document.getElementById("bug-total").innerHTML = "Total number of bugs: " + bug_total;
            document.getElementById("tag-total").innerHTML = "Total number of tags: " + tag_total;
        }

        $(document).ready(function(){
            // Expand Panel
            $("#open").click(function(){ $("div#panel").slideDown("slow"); });

            // Collapse Panel
            $("#close").click(function(){ $("div#panel").slideUp("slow"); });

            // Switch buttons on the tab from "Options" to "Close"
            $("#toggle a").click(function () { $("#toggle a").toggle(); });

            tag_values_handler(null, null, false);
            importance_handler(null, null, false);
            status_handler(null, null, false);

            /*
            assignee_handler(null, null, false);
            date_handler(null, null, false);
            */
            update_tables();
        });
    </script>

</html>
<!-- vi:set ts=4 sw=4 expandtab syntax=mako: -->
