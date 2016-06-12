from django.conf.urls import include, url
from django.contrib import admin

#from provider.views import ProvierListView

urlpatterns = [
    #url(r'^api/',include('api.urls')),
    url(r'^polygon/', include('api.polygon.urls')),
    url(r'^provider/', include('api.provider.urls')),       
]
