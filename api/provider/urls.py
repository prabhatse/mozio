from django.conf.urls import include, url
from django.contrib import admin

from .views import (
	ProviderListAPIView,
    ProviderRetrieveAPIView,
	ProviderDeleteAPIView,
	ProviderUpdateAPIView,
	ProviderCreateAPIView
	)

urlpatterns = [
    #url(r'^api/',include('api.urls')),
    url(r'^$', ProviderListAPIView.as_view()),
    url(r'^all/$', ProviderListAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', ProviderRetrieveAPIView.as_view()),
    url(r'^create/$',ProviderCreateAPIView.as_view()),
    url(r'^(?P<id>\d+)/update/$',ProviderUpdateAPIView.as_view()),
    url(r'^(?P<id>\d+)/delete/$',ProviderDeleteAPIView.as_view()),
    #url(r'^$', include('urls')),       
]