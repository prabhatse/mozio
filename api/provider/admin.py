from django.contrib import admin

from .models import Providers

class ProvidersModelAdmin(admin.ModelAdmin):
	list_display = ["__str__", "name","email"]
	list_filter = ["created"]
	class Meta:
		model = Providers
		
admin.site.register(Providers, ProvidersModelAdmin)