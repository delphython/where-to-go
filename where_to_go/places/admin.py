from django.contrib import admin

from adminsortable2.admin import SortableInlineAdminMixin

from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["image_preview"]
    fields = ("image_file", "image_preview", "image_order")


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        return obj.image_preview

    readonly_fields = ["image_preview"]
    fields = ("image_file", "image_preview", "image_order")

    image_preview.short_description = "Image Preview"
    image_preview.allow_tags = True
