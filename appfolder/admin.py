from django.contrib import admin

# Register your models here.
from .models import MovieModel

admin.site.register(MovieModel)
