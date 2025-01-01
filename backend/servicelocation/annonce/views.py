from rest_framework import viewsets  # Importation de la classe viewsets de Django REST framework
from .models import Location, Characteristic  # Importation des modèles Location et Characteristic
from .serializers import LocationSerializer, CharacteristicSerializer  # Importation des serializers correspondants

# Définition de la vue pour le modèle Location
class LocationViewSet(viewsets.ModelViewSet):
    """
    Cette vue permet de gérer les opérations CRUD pour le modèle Location.
    Elle utilise un ModelViewSet, qui fournit automatiquement les actions 'list', 'create', 'retrieve', 'update' et 'destroy'.
    """
    queryset = Location.objects.all()  # Récupération de tous les objets Location de la base de données
    serializer_class = LocationSerializer  # Utilisation du serializer LocationSerializer pour la validation et la transformation des données

# Définition de la vue pour le modèle Characteristic
class CharacteristicViewSet(viewsets.ModelViewSet):
    """
    Cette vue permet de gérer les opérations CRUD pour le modèle Characteristic.
    Elle utilise un ModelViewSet, qui fournit automatiquement les actions 'list', 'create', 'retrieve', 'update' et 'destroy'.
    """
    queryset = Characteristic.objects.all()  # Récupération de tous les objets Characteristic de la base de données
    serializer_class = CharacteristicSerializer  # Utilisation du serializer CharacteristicSerializer pour la validation et la transformation des données

