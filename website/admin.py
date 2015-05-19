from django.contrib import admin
from .models import Movie, Projection, Reservation

# Register your models here.


admin.site.register(Movie)
admin.site.register(Projection)
admin.site.register(Reservation)
