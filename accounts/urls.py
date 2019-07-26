from django.urls import path
from django.conf.urls import url, include
from . import views
urlpatterns=[
url(r'^$', views.home, name="home"),
url(r'^login', views.login, name="login"),
url(r'^createclassinformation', views.createclassinformation, name="createclassinformation"),
url(r'^editclassinformation/(?P<pk>\d+)', views.editclassinformation, name="editclassinformation"),
url(r'^deleteclassinformation', views.deleteclassinformation, name="deleteclassinformation"),
url(r'^viewclassinformation', views.viewclassinformation, name="viewclassinformation"),
url(r'^logout', views.login, name="logout")
]
