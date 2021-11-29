from biofloc.models import Build_tank, Newsletter
from django.contrib import admin

# Register your models here.
admin.site.register(Newsletter)


@admin.register(Build_tank)
class Build_tankAdmin(admin.ModelAdmin):
    list_display = ['tanks', 'water', 'fish', 'food']
