from django.contrib import admin

# Register your models here.
from .models import Pipeline

class CryptoFileModelAdmin(admin.ModelAdmin):
	list_display = ["name", "longitude", "latitude", "is_damaged", "damage_grade","updated"]
	list_display_links = ["name"]
	list_editable = ["longitude","latitude"]
	# list_filter = ["updated", "timestamp"]

	search_fields = ["name"]
	class Meta:
		model = Pipeline


admin.site.register(Pipeline, CryptoFileModelAdmin)