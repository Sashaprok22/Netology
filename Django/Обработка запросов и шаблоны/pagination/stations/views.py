import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

stations = None
def get_stations():
    global stations
    if stations: return stations

    with open(settings.BUS_STATION_CSV, "r", encoding="utf-8") as file:
        csv_result = list(csv.reader(file))
        stations = [dict(zip(csv_result[0], station)) for station in csv_result[1:]]

    return stations

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    paginator = Paginator(get_stations(), 30)
    page_num = int(request.GET.get("page", 1))
    page = paginator.get_page(page_num)

    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)
