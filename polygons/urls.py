from django.conf.urls import include, url


from . import views


urlpatterns = [
	url(r'^$', views.service_area_set, name="index"),
    url(r'^find/$', views.find_service_area, name="find"),
    url(r'^get_polygons/$', views.get_service_area, name="get_polygons"),
    url(r'^get_polygons/(?P<service_area>\d+)$', views.get_service_area, name="get_polygons"),

	]

