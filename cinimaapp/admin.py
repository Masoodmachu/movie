from django.contrib import admin
from cinimaapp.models import Movie
from cinimaapp.models import CustomUser



# Register your models here.

admin.site.register(Movie)
admin.site.register(CustomUser)