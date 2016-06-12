from django.contrib import admin

from .models import ServiceAreaPolygon

class ServiceAreaPolygonAdmin(admin.ModelAdmin):
	list_display = ["__str__", "name"]
	class Meta:
		model = ServiceAreaPolygon

admin.site.register(ServiceAreaPolygon, ServiceAreaPolygonAdmin)