from django.db import models
from django.utils.html import mark_safe


class Place(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    description_short = models.CharField("Краткое описание", max_length=255)
    description_Long = models.TextField("Полное описание")
    coordinates_lng = models.CharField("Координаты долгота", max_length=17)
    coordinates_lat = models.CharField("Координаты широта", max_length=17)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        to="places.Place",
        verbose_name="Куда пойти",
        on_delete=models.PROTECT,
    )
    image_file = models.ImageField("Картинка")
    image_order = models.IntegerField("Порядок сортировки")

    def __str__(self):
        return f"{self.image_order} {self.place}"

    @property
    def image_preview(self):
        if self.image_file:
            return mark_safe(
                '<img src="{}" height="200" />'.format(self.image_file.url)
            )
        return ""
