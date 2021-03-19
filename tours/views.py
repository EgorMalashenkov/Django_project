from django.shortcuts import render
from data import departures, tours


def main_view(request):
    return render(request, 'tours/index.html', departures)


def depature_view(request):
    return render(request, 'tours/departure.html', {'departures': departures})


def tour_view(request):
    return render(request, 'tours/tours.html')

# Create your views here.
