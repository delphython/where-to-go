from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .models import Place


def serialize_place_properties(place):
    imgs = [images.image_file.url for images in place.images.all()]

    place_properties = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": str(place.coordinates_lng),
            "lng": str(place.coordinates_lat),
        },
    }

    return place_properties


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
                    "placeId": place.id,
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

    return JsonResponse(
        serialize_place_properties(place),
        safe=False,
        json_dumps_params={
            "ensure_ascii": False,
            "indent": 4,
        },
    )
