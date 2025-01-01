from rest_framework import serializers
from .models import Location, Appartement, Studio, Villa

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = '__all__'
		#
	#
#
class AppartementSerializer(LocationSerializer):
	class Meta(LocationSerializer.Meta):
		model = Studio
		#
	#
#
class StudioSerializer(LocationSerializer):
	class Meta(LocationSerializer.Meta):
		model = Studio
		#
	#
#
class VillaSerializer(LocationSerializer):
	class Meta(LocationSerializer.Meta):
		model = Villa
