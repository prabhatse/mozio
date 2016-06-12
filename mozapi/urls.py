from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mozapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^polygon/', include('polygons.urls')),
    url(r'^provider/', include('providers.urls')),
    url(r'^api-docs/', include('rest_framework_swagger.urls')),
    ]
