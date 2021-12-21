import uuid

from django.shortcuts import render

from .models import Place


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
                    "detailsUrl": "",
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
