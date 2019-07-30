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
url(r'^logout', views.login, name="logout")
]
