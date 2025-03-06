#http://127.0.0.1:8000/meteo/index/
# run python3 manage.py runserver

import matplotlib
matplotlib.use('Agg')
from django.shortcuts import render
from django.http import HttpResponse
import io
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from django.conf import settings
import logging
from rolls.TemprePlot import TempPLT, BarPlot

logger = logging.getLogger(__name__)

def index(request):
    from rolls.models import TempModel  # Local import
    return render(request, 'rolls/index.html', {'temp_data': TempModel.objects.all()})

def meteo(request):
    return render(request, 'rolls/meteo.html')

def temperature_min_max(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'rolls/stazione.csv')
    try:
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        return HttpResponse(f"Error reading CSV file: {e}", status=500)

    x = df['Temperatura_media']
    y = df['Temperatura_massima']
    
    return TempPLT.plotter("Temperatura massima e minima", "minima", "massima", x, y)

def temperatura_media(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'rolls/stazione.csv')
    try:
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        return HttpResponse(f"Error reading CSV file: {e}", status=500)

    x = df['Giorno']
    y = df['Temperatura_media']

    return TempPLT.plotter("Temperature", "Giorni", "Temperatura", x, y)

def temperatura_max_umidita(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'rolls/stazione.csv')
    try:
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        return HttpResponse(f"Error reading CSV file: {e}", status=500)

    x = df['Giorno']
    y = df['Temperatura_media']

    return BarPlot.Barplotter('Temperatura Umidita', 'Temp max [C°]', 'Umidita', x, y)
