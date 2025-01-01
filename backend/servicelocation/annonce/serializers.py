from rest_framework import serializers
from .models import Location, Characteristic

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = '__all__'

