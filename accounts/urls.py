from django.urls import path
from django.conf.urls import url, include
from . import views
urlpatterns=[
url(r'^$', views.home, name="home"),
url(r'^login', views.login, name="login"),
url(r'^createclassinformation', views.createclassinformation, name="createclassinformation"),
url(r'^editclassinformation/(?P<pk>\d+)', views.editclassinformation, name="editclassinformation"),
url(r'^deleteclassinformation/(?P<pk>\d+)', views.deleteclassinformation, name="deleteclassinformation"),
url(r'^viewclassinformation', views.viewclassinformation, name="viewclassinformation"),

url(r'^createsectioninformation', views.createsectioninformation, name="createsectioninformation"),
url(r'^editsectioninformation/(?P<pk>\d+)', views.editsectioninformation, name="editsectioninformation"),
url(r'^deletesectioninformation/(?P<pk>\d+)', views.deletesectioninformation, name="deletesectioninformation"),
url(r'^viewsectioninformation', views.viewsectioninformation, name="viewsectioninformation"),

url(r'^createteacher', views.createteacher, name="createteacher"),
url(r'^editteacher/(?P<pk>\d+)', views.editteacher, name="editteacher"),
url(r'^deleteteacher/(?P<pk>\d+)', views.deleteteacher, name="deleteteacher"),
url(r'^viewteachers', views.viewteachers, name="viewteachers"),

url(r'^addsubject', views.addsubject, name="addsubject"),
url(r'^editsubject/(?P<pk>\d+)', views.editsubject, name="editsubject"),
url(r'^deletesubject/(?P<pk>\d+)', views.deletesubject, name="deletesubject"),
url(r'^viewsubjects', views.viewsubjects, name="viewsubjects"),

url(r'^addsyllabus', views.addsyllabus, name="addsyllabus"),
url(r'^editsyllabus/(?P<pk>\d+)', views.editsyllabus, name="editsyllabus"),
url(r'^deletesyllabus/(?P<pk>\d+)', views.deletesyllabus, name="deletesyllabus"),
url(r'^viewsyllabus', views.viewsyllabus, name="viewsyllabus"),

url(r'^addhumanresource', views.addhumanresource, name="addhumanresource"),
url(r'^edithumanresource/(?P<pk>\d+)', views.edithumanresource, name="edithumanresource"),
url(r'^deletehumanresource/(?P<pk>\d+)', views.deletehumanresource, name="deletehumanresource"),
url(r'^viewhumanresource', views.viewhumanresource, name="viewhumanresource"),

url(r'^addroutine', views.addroutine, name="addroutine"),
url(r'^editroutine/(?P<pk>\d+)', views.editroutine, name="editroutine"),
url(r'^deleteroutine/(?P<pk>\d+)', views.deleteroutine, name="deleteroutine"),
url(r'^viewroutine', views.viewroutine, name="viewroutine"),

url(r'^addassignment', views.addassignment, name="addassignment"),
url(r'^editassignment/(?P<pk>\d+)', views.editassignment, name="editassignment"),
url(r'^deleteassignment/(?P<pk>\d+)', views.deleteassignment, name="deleteassignment"),
url(r'^viewassignment', views.viewassignment, name="viewassignment"),

url(r'^addexamgrade', views.addexamgrade, name="addexamgrade"),
url(r'^editexamgrade/(?P<pk>\d+)', views.editexamgrade, name="editexamgrade"),
url(r'^deleteexamgrade/(?P<pk>\d+)', views.deleteexamgrade, name="deleteexamgrade"),
url(r'^viewexamgrade', views.viewexamgrade, name="viewexamgrade"),

url(r'^addexamterm', views.addexamterm, name="addexamterm"),
url(r'^editexamterm/(?P<pk>\d+)', views.editexamterm, name="editexamterm"),
url(r'^deleteexamterm/(?P<pk>\d+)', views.deleteexamterm, name="deleteexamterm"),
url(r'^viewexamterm', views.viewexamterm, name="viewexamterm"),

url(r'^addexamschedule', views.addexamschedule, name="addexamschedule"),
url(r'^editexamschedule/(?P<pk>\d+)', views.editexamschedule, name="editexamschedule"),
url(r'^deleteexamschedule/(?P<pk>\d+)', views.deleteexamschedule, name="deleteexamschedule"),
url(r'^viewexamschedule', views.viewexamschedule, name="viewexamschedule"),

url(r'^addexamsuggestion', views.addexamsuggestion, name="addexamsuggestion"),
url(r'^editexamsuggestion/(?P<pk>\d+)', views.editexamsuggestion, name="editexamsuggestion"),
url(r'^deleteexamsuggestion/(?P<pk>\d+)', views.deleteexamsuggestion, name="deleteexamsuggestion"),
url(r'^viewexamsuggestion', views.viewexamsuggestion, name="viewexamsuggestion"),

url(r'^addlibrarybook', views.addlibrarybook, name="addlibrarybook"),
url(r'^editlibrarybook/(?P<pk>\d+)', views.editlibrarybook, name="editlibrarybook"),
url(r'^deletelibrarybook/(?P<pk>\d+)', views.deletelibrarybook, name="deletelibrarybook"),
url(r'^viewlibrarybook', views.viewlibrarybook, name="viewlibrarybook"),

url(r'^addvehicle', views.addvehicle, name="addvehicle"),
url(r'^editvehicle/(?P<pk>\d+)', views.editvehicle, name="editvehicle"),
url(r'^deletevehicle/(?P<pk>\d+)', views.deletevehicle, name="deletevehicle"),
url(r'^viewvehicle', views.viewvehicle, name="viewvehicle"),

url(r'^addroute', views.addroute, name="addroute"),
url(r'^editroute/(?P<pk>\d+)', views.editroute, name="editroute"),
url(r'^deleteroute/(?P<pk>\d+)', views.deleteroute, name="deleteroute"),
url(r'^viewroute', views.viewroute, name="viewroute"),

url(r'^addhostel', views.addhostel, name="addhostel"),
url(r'^edithostel/(?P<pk>\d+)', views.edithostel, name="edithostel"),
url(r'^deletehostel/(?P<pk>\d+)', views.deletehostel, name="deletehostel"),
url(r'^viewhostel', views.viewhostel, name="viewhostel"),

url(r'^addroom', views.addroom, name="addroom"),
url(r'^editroom/(?P<pk>\d+)', views.editroom, name="editroom"),
url(r'^deleteroom/(?P<pk>\d+)', views.deleteroom, name="deleteroom"),
url(r'^viewroom', views.viewroom, name="viewroom"),
url(r'^logout', views.login, name="logout")
]
