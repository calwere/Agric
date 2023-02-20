from django.contrib import admin
from .models import Incidences
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class IncidencesAdmin(LeafletGeoAdmin):
    #pass
    list_display = ('name', 'location')

admin.site.register(Incidences, IncidencesAdmin)
# admin.site.register(Roads)

STATIC_URL = '/static'
