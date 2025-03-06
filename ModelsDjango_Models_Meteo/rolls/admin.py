from django.contrib import admin
from .models import TempModel 
# Register your models here.

'''

python manage.py makemigrations
python manage.py migrate
python manage.py flush

'''

admin.site.register(TempModel)


