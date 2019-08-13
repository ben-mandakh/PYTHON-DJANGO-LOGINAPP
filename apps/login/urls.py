from django.conf.urls import url
from . import views	

urlpatterns = [
        url(r'^$', views.index),
        url(r'^process$', views.process),
        url(r'^success$', views.success),
        url(r'^login$', views.login),
        # url(r'^shows/(?P<id>\d+)$', views.show_one),
        # url(r'^shows/(?P<id>\d+)/edit$', views.editShow),
        # url(r'^shows/(?P<id>\d+)/update$', views.editShowFunction),
        # url(r'^shows/(?P<id>\d+)/delete$', views.delete),
        # url(r'^shows/update$', views.editShowFunction),
]