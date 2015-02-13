#!/usr/bin/python

from launchpadlib.launchpad import Launchpad
from launchpadlib.errors import HTTPError
from launchpadlib.credentials import Credentials
from operator import attrgetter
import datetime
from datetime import datetime, date
import time
import sys, os
import optparse
import shutil
import re

def move_report(report):
    if os.path.exists(home + report):
        if os.path.exists(repository + report):
            os.remove(repository + report)
        shutil.move(home + report, repository)

def create_page(page, title, packages):
    datafile = open(home + page, 'w')
    templatefile = open(template, 'r')
    bugcount = 0

    for line in templatefile:
        if line.strip() == "<!-- *** Title Space *** -->":
            datafile.write("Desktop Team Bugs Summary Page")
        elif line.strip() == "<!-- *** Title *** -->":
            datafile.write(title)
        elif line.strip() == "<!-- *** Table Header Space *** -->":
            datafile.write("<th></th><th>Bug Number</th><th colspan=\"2\">Summary</th><th>Source</th><th>Importance</th><th>Status</th><th>Users affected</th><th>Duplicates</th><th>Heat</th><th>Assignee</th>")
        elif line.strip() == "<!-- *** Table Body Space *** -->":
            for package in packages:
                p = release.getSourcePackage(name=package)
                for task in p.searchTasks(omit_targeted=False):
                    try:
                        table_row = "<tr>"
                        table_row += "<td class=\"icon right\"><span alt=\"(undecided)\" title=\"Undecided\" class=\"sprite bug-%s\">&nbsp;</span></td>" % (task.importance.encode('utf-8').lower())
                        
                        table_row += "<td class=\"amount\">%s</td>" % task.bug.id
                        try:
                            table_row += "<td><a href='http://launchpad.net/bugs/%s'>%s</a></td>" % (task.bug.id, task.bug.title.encode('utf-8'))
                        except:
                            table_row += "<td><a href='http://launchpad.net/bugs/%s'>Can't decode title</a></td>" % (task.bug.id)
                        table_row += "<td align=\"right\" style=\"padding-right: 5px\"></td>"
                        package_name = re.sub('\ \(Ubuntu Oneiric\)','', task.bug_target_display_name)
                        table_row += '<td><a href=\"https://bugs.launchpad.net/ubuntu/+source/%s">%s</td>\n' % (package_name.encode('utf-8'), package_name.encode('utf-8'))
                        table_row += "<td class=\"importance%s\">%s</td>" % (task.importance.encode('utf-8').upper(), task.importance.encode('utf-8'))
                        table_row += "<td class=\"status%s\">%s</td>" % (task.status.encode('utf-8').upper().replace(" ",""), task.status.encode('utf-8'))
                        table_row += "<td>%s</td>" % task.bug.users_affected_count
                        table_row += "<td>%s</td>" % task.bug.number_of_duplicates
                        table_row += "<td>%s</td>" % task.bug.heat
                        if task.assignee:
                            table_row += "<td><a href=\"http://launchpad.net/~%s\">%s</td>" % (task.assignee.name.encode('utf-8'), task.assignee.display_name.encode('utf-8'))
                        else:
                            table_row += "<td>None</td>"
                        table_row += "</tr>"
                        table_row += "\n"
                        bugcount+=1
                        datafile.write(table_row)
                    except HTTPError, error:
                        print "There was an error with bug %s: %s" % (task.title.split(' ')[1].replace('#',''), error)
        elif line.strip() == "<!-- *** Last Paragraph Space *** -->":
            datafile.write("<b>Packages being tracked:</b><br/>")
            #for software in packages:
            #    datafile.write("%s <br/>" % software)
        elif line.strip() == "<!-- *** Updated on *** -->":
            date_now = datetime.utcnow()
            datafile.write("<strong>Updated on: %s</strong>" % date_now)
        else:
            datafile.write(line)
    datafile.close()
    move_report(os.path.basename(datafile.name))

home = os.getenv('HOME') + "/scripts/"
repository = '/srv/qa.ubuntu.com/reports/ubuntu-desktop/'
template = home + 'template.html' 
highlist = []
cachedir = os.path.expanduser("/home/pedro/.launchpadlib/cache/")
root = 'production'

if not os.path.exists(cachedir):
    os.makedirs(cachedir, 0700)

root = 'production'
version = "devel"
script_name = sys.argv[0].split("/")[-1].split('.')[0]

credfile = os.path.expanduser('/home/pedro/.launchpadlib/%s.cred' % script_name)
launchpad = Launchpad.login_with(script_name, service_root=root, launchpadlib_dir=cachedir, credentials_file=credfile, version=version)

ubuntu = launchpad.distributions["ubuntu"]
release = ubuntu.getSeries(name_or_version='oneiric')

#get the list of packages in desktop-bugs
team = launchpad.people['desktop-bugs']
packages = team.getBugSubscriberPackages()

#list of individual packages. 
other_packages = ['gwibber', 'telepathy-butterfly', 'telepathy-gabble', 'telepathy-haze', 'telepathy-idle', 'network-manager', 'lightdm', 'network-manager-applet', 'libreoffice', 'language-selector', 'deja-dup', 'couchdb-glib', 'evolution-couchdb', 'banshee', 'thunderbird', 'firefox', 'zeitgeist', 'libzeitgeist', 'zeitgeist-filesystem', 'zeitgeist-sharp', 'zeitgeist-datasources', 'sezen', 'gnome-activity-journal', 'zeitgeist-extensions']

paquete = []

for p in packages:
    paquete.append(p.name)

for p in other_packages:
    paquete.append(p)

create_page('oneiric.html', 'Oneiric Bugs', paquete)
