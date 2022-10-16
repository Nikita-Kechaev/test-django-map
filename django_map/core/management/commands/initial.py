import pandas as pd
from core.models import City
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand

tmp_data_city = pd.read_csv(
    'core/management/commands/city.csv', sep=',', encoding="utf-8"
)
tmp_data_city['city'] = tmp_data_city['city'].fillna(tmp_data_city['region'])


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, **options):
        cities = [
            City(
                name=row['city'],
                location=Point(row['geo_lon'], row['geo_lat']),
            )
            for _, row in tmp_data_city.iterrows()
        ]

        City.objects.bulk_create(cities, ignore_conflicts=True)
