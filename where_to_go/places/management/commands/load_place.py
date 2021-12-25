import requests

from django.core.management.base import BaseCommand

from places.models import Place, Image


def get_place_json_properties(json_url):
    response = requests.get(json_url)
    response.raise_for_status()

    print(response.json())

    return response.json()


def insert_place_to_db(place):
    Place.objects.get_or_create(
        title=place["title"],
        description_short=place["description_short"],
        description_Long=place["description_long"],
        coordinates_lng=place["coordinates"][0],
        coordinates_lat=place["coordinates"][0],
    )


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str)

    def handle(self, *args, **options):
        insert_place_to_db(get_place_json_properties(options["json_file"]))
