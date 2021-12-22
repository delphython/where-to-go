import json
import uuid

from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .models import Place, Image


def get_place_properties(place):
    imgs = [
        images.image_file.url for images in Image.objects.filter(place=place)
    ]

    url_details = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.description_short,
        "description_long": place.description_Long,
        "coordinates": {
            "lat": place.coordinates_lng,
            "lng": place.coordinates_lat,
        },
    }

    return url_details


def index(request):
    features = []

    places = Place.objects.all()

    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        place.coordinates_lng,
                        place.coordinates_lat,
                    ],
                },
                "properties": {
                    "title": place.title,
                    "placeId": uuid.uuid4(),
                    "detailsUrl": reverse("details-url", args=[place.id]),
                },
            }
        )

    geo_json_places = {
        "type": "FeatureCollection",
        "features": features,
    }

    context = {
        "places": geo_json_places,
    }

    return render(request, "index.html", context=context)


def place_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    return HttpResponse(
        json.dumps(
            get_place_properties(place),
            ensure_ascii=False,
            indent=4,
        ),
        content_type="application/json",
    )
