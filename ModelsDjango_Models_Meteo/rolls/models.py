from django.db import models
from rolls.views import temperature_min_max


#python3 manage.py makemigrations 
#python3 manage.py migrate
#python3 manage.py createsuperuser
#python3 manage.py runserver 
#rolls/migrations/0001_initial.py

'''
class Meteo(models.Model):
    immagine=models.ImageField()
'''
'''
class TempModel(models.Model):  
    giorno = models.DateField()  
    temperatura_media = models.FloatField()  

    def __str__(self):
        return f"{self.giorno}: {self.temperatura_media}°C"

'''

#Creazione del modello database Django



class TempModel(models.Model):
    giorno = models.DateField()
    temperatura_media = models.FloatField()

    def __str__(self):
        return f"{self.giorno}: {self.temperatura_media}°C"

