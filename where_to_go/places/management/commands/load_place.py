import os
from urllib.parse import urlparse, unquote

import requests

from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from places.models import Place, Image


def get_file_name(url):
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    _, file_name = os.path.split(path)

    return file_name


def get_image_file(image_url):
    response = requests.get(image_url)
    response.raise_for_status()

    img_temp = NamedTemporaryFile()
    img_temp.write(response.content)
    img_temp.flush()

    return File(img_temp)


def get_place_properties(json_url):
    response = requests.get(json_url)
    response.raise_for_status()

    return response.json()


def add_place(place_properties):
    place, is_created = Place.objects.get_or_create(
        title=place_properties["title"],
        defaults={
            "description_short": place_properties["description_short"],
            "description_long": place_properties["description_long"],
            "coordinates_lng": place_properties["coordinates"]["lng"],
            "coordinates_lat": place_properties["coordinates"]["lat"],
        },
    )

    if is_created:
        for image_url in place_properties["imgs"]:
            image = Image(place=place)
            image.image_file.save(
                get_file_name(image_url), get_image_file(image_url), save=True
            )


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str)

    def handle(self, *args, **options):
        add_place(get_place_properties(options["json_file"]))
