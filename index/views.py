from django.shortcuts import render
from .models import about
from .models import slider
from .models import client


def home(request):
    about_data = about.objects.all()[0]
    slider_data = slider.objects.all()
    client_data = client.objects.all()
    context = {
        'about': about_data,
        'slider': slider_data,
        'client': client_data
    }
    return render(request, 'index.html', context)


def aboutus(request):
    return render(request, 'about.html')
