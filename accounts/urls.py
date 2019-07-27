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
url(r'^logout', views.login, name="logout")
]
