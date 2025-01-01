from django.contrib import admin  # Importation de l'admin de Django
from .models import Location, Characteristic  # Importation des modèles Location et Characteristic

# Enregistrement du modèle Location dans l'admin
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('typeLocation', 'address', 'city', 'price', 'bailleur_id', 'location')  # Champs à afficher dans la liste des locations
    search_fields = ('typeLocation', 'city', 'address')  # Champs sur lesquels effectuer des recherches

# Enregistrement du modèle Characteristic dans l'admin
@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'location')  # Champs à afficher dans la liste des caractéristiques
    search_fields = ('name',)  # Champs sur lesquels effectuer des recherches
