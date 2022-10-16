from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import City


@admin.register(City)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
    search_fields = ['name', ]
