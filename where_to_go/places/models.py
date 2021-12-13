from django.db import models


class Place(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    description_short = models.CharField("Краткое описание", max_length=200)
    description_Long = models.TextField("Полное описание")
    coordinates_lng = models.CharField("Координаты долгота", max_length=17)
    coordinates_lat = models.CharField("Координаты широта", max_length=17)

    def __str__(self):
        return self.title
