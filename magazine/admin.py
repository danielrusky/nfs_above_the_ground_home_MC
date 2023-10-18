from django.contrib import admin

from magazine.models import Autocar, Marka


@admin.register(Autocar)
class AutocarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'marka',)
    list_filter = ('marka',)
    search_fields = ('name', 'description',)


@admin.register(Marka)
class MarkaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)