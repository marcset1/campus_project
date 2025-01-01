from rest_framework import serializers
from .models import Client, Notification

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'username', 'email', 'password', 'telephone', 'adresse']
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        client = Client.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            telephone=validated_data.get('telephone'),
            adresse=validated_data.get('adresse')
        )
        return client
		#
	#
#
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'client', 'message', 'date_created', 'sent']

