import folium
from dadata import Dadata
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.shortcuts import redirect, render
import os

from .forms import FindForm
from .models import City


def main(request):
    template = 'core/main.html'
    form = FindForm()
    map = folium.Map(zoom_start=7)

    if request.method == 'POST':
        form = FindForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']

            token = os.getenv('DADATA_TOKEN')
            secret = os.getenv('DADATA_SECRET')

            dadata = Dadata(token, secret)

            try:
                result = dadata.clean("address", city_name)
            except:
                result = {
                    'city': city_name,
                    'result': None,
                    'country': 'Россия',
                    'postal_code': 'Невозможно получить, dadata не отвечает'
                }

            city_name = result['city']
            if result['city'] is None:
                city_name = result['region']

            radius = form.cleaned_data['radius']

            try:
                city = City.objects.get(name=city_name)
            except:
                if result['result'] is None:
                    return redirect('/')

                point = Point(
                        float(result['geo_lon']),
                        float(result['geo_lat']))

                if City.objects.filter(location=point).exists():
                    City.objects.get(location=point).delete()

                city = City.objects.create(
                    name=result['region'],
                    location=point
                )

            folium.Marker(
                location=[city.location.y, city.location.x],
                popup=f"{result['postal_code']}, "
                      f"{city_name}, {result['country']}",
                icon=folium.Icon(color='green')
            ).add_to(map)

            if radius:
                qs = City.objects.filter(
                    location__distance_lt=(
                        city.location, Distance(km=radius))).exclude(
                            id=city.id)
                for elem in qs:
                    folium.Marker(
                        location=[elem.location.y, elem.location.x],
                        popup=elem.name,
                        icon=folium.Icon(color='red')
                    ).add_to(map)

    map = map._repr_html_()
    context = {
        'map': map,
        'form': form
    }
    return render(request, template, context)


def project(request):
    template = 'core/project.html'
    return render(request, template)


def autor(request):
    template = 'core/autor.html'
    return render(request, template)
