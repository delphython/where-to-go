from django.contrib import admin

from places.models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description_short",
        "description_Long",
        "coordinates_lng",
        "coordinates_lat",
    )
