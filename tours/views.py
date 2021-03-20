import random
from django.shortcuts import render
from tours import data


def main_view(request):
    number = random.randint(0, 30)
    tours = random.sample(data.tours.items(), 6)
    return render(request, 'tours/index.html',
                  context={'title': data.title,
                           'subtitle': data.subtitle,
                           'description': data.description,
                           'tours': tours,
                           'departures': data.departures})


def depature_view(request):
    return render(request, 'tours/departure.html', {'departures': data.departures})


def tour_view(request):
    return render(request, 'tours/tours.html', {'departures': data.departures})

# Create your views here.
