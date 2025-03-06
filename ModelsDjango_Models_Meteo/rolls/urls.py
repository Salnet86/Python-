#configurazione delle urlpatterns 
from django.urls import path
from . import views 

app_name = 'rolls'

urlpatterns = [
    path('index/', views.index, name='index'),  
    path('MT/', views.meteo, name='meteo'),     
    path('temperature_min_max/', views.temperature_min_max, name='temperature_min_max'),
    path('temperatura_media/', views.temperatura_media, name='temperatura_media'),
    path('temperatura_max_umidita/', views.temperatura_max_umidita, name='temperatura_max_umidita'),
    
]