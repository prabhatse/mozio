from django.conf.urls import include, url
from django.contrib import admin

from .views import (
    PolygonListAPIView,
    PolygonRetrieveAPIView,
	PolygonSearchAPIView,
	PolygonDeleteAPIView,
	PolygonUpdateAPIView,
	PolygonCreateAPIView
	)

urlpatterns = [
    #url(r'^api/',include('api.urls')),
    url(r'^$', PolygonListAPIView.as_view()),
    url(r'^all/$', PolygonListAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', PolygonRetrieveAPIView.as_view()),
    url(r'^search/$', PolygonSearchAPIView.as_view()),
    url(r'^create/$',PolygonCreateAPIView.as_view()),
    url(r'^(?P<id>\d+)/update/$',PolygonUpdateAPIView.as_view()),
    url(r'^(?P<id>\d+)/delete/$',PolygonDeleteAPIView.as_view()),
    #url(r'^$', include('urls')),       
]