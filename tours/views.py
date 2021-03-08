from django.shortcuts import render


def MainView(request):
    return render(request, 'index.html')


def DepartureView(request):
    return render(request, 'departure.html')


def TourView(request):
    return render(request, 'tours.html')

# Create your views here.
