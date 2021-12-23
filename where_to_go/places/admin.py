from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ("image_file", "headshot_image", "image_order")
    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.headshot.url,
                width=obj.headshot.width,
                height=obj.headshot.height,
            )
        )
