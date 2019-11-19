from django.contrib import admin

# Register your models here.

from . models import Tipo, Sala, Arriendo

admin.site.register(Tipo)
admin.site.register(Sala)
admin.site.register(Arriendo)
