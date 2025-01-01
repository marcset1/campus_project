# myproject/models.py
from django.db import models

class Client(models.Model):
	# Pseudo unique pour chaque client
	pseudo = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=25, null=False)
	# Adresse du client (optionnelle)
	adresse = models.CharField(max_length=255, blank=True, null=True)
	# Email unique du client (optionnel)
	email = models.EmailField(unique=True, blank=True, null=True)
	# Numéro de téléphone du client (optionnel)
	telephone = models.CharField(max_length=15, blank=True, null=True)
	# Préférences alimentaires sous forme de JSON
	#preferences_alimentaires = models.JSONField(null=True)  # Ex: {"legumes": True, "fruits": False, "viande": True, "poisson": False}
	# Préférences sonores sous forme de JSON
	#preferences_sonore = models.JSONField(null=True)  # Ex: {"ambiance": True, "silence": False, "calme": True, "guerre": False}
	last_login = models.DateTimeField(null=True, blank=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	
    # Surcharge de la méthode save pour vérifier qu'au moins un email ou un numéro de téléphone est fourni
	#def save(self, *args, **kwargs):
		#if not self.email and not self.telephone:
			#raise ValueError("Le client doit avoir au moins un numéro de téléphone ou un email.")
		#self.save()
		#
	#
	def __str__(self):
		return f"my name is {self.pseudo} and my password is {self.password}"
		#
	#
#
class Bailleur(Client):
	cni = models.CharField(max_length=20, verbose_name="immatriculation de la cni", null=False)
	presentation = models.TextField(max_length=150, verbose_name="une brieve presentation du bailleur")
	
	def __str__(self):
		return f"my name is {self.pseudo} and my password is {self.password}. presentation:{self.presentation}"
#
class Notification(models.Model):
	not_client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='notifications_client')
	not_bailleur_id = models.ForeignKey(Bailleur, on_delete=models.CASCADE, related_name='notifications_bailleur')
	message = models.TextField(max_length=500, null=False)
