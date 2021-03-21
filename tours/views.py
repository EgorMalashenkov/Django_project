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
                           'departures': data.departures,
                           })


def depature_view(request, departure_id):
    current_departures = {
        tour_id: tour for tour_id, tour in data.tours.items() if tour['departure'] == departure_id}
    return render(request, 'tours/departure.html', context={'departures': data.departures,
                                                            'city': data.departures[departure_id].split()[1],
                                                            'tours': current_departures,

                                                            })


def tour_view(request, tour_id):
    return render(request, 'tours/tours.html', context={'tour': data.tours[tour_id],
                                                        'departure': data.tours[tour_id]['departure'],
                                                        'country': data.tours[tour_id]['country'],
                                                        'title': data.tours[tour_id]['title'],
                                                        'departures': data.departures,
                                                        'description': data.tours[tour_id]['description'],
                                                        'price': data.tours[tour_id]['price'],
                                                        'city': data.departures[data.tours[tour_id]['departure']],
                                                        "nights": data.tours[tour_id]["nights"]
                                                        })


# Create your views here.
