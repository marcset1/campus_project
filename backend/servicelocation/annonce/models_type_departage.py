from django.db import models

class Location(models.Model):
	lieu = models.CharField(max_length=50)
	localisation = models.CharField(max_length=255)
	idBailleur = models.PositiveIntegerField()
	status = models.BooleanField(default=False)
	datepub = models.DateTimeField(auto_now=True)
	placard = models.BooleanField(default=False)
	toiletteExt = models.BooleanField(default=False)
	toiletteInt = models.BooleanField(default=False)
	
	def __str__(self):
		return f"location du bailleur {self.idBailleur} au prix de {self.prix} situe a {self.lieu}"
		#
	#
#
class Appartement(Location):
	""" 1 salon, toilettes, cuisine, chambres """
	
	nbtoilette = models.PositiveIntegerField()
	nbChambre = models.PositiveIntegerField()
	
	#
class Studio(Location):
	""" 1 chambre(piece), toilette, placards """
	
	nbtoilette = models.PositiveIntegerField()
	#
#
class Villa(Location):
	""" chambres, toilettes, etages, cuisines,  """
	
	nbChambre = models.PositiveIntegerField()
	nbSalon = models.PositiveIntegerField()
	nbCuisine = models.PositiveIntegerField()                                                                                                                                                                                                                                                                                                                   
	#
#


class Media(models.Model):
	""" installer pillow: pip install pillow puis: MEDIA_ROOT dans settings.py """
	label = models.CharField(max_length=100) 
	
	def __self__(self):
		return f"je suis le media {self.label} de la location {self.location}"
		#
	#
class MediaAppart(Media):
	photo = models.ImageField(upload_to='photos/apparts')
	idLocation = models.ForeignKey('Appartement', on_delete=models.CASCADE) # id du dernier appartment ajoutee par l'user dans la classe Appartement
	#
#
class MediaStudio(Media):
	photo = models.ImageField(upload_to='photos/Studios')
	idLocation = models.ForeignKey('Studio', on_delete=models.CASCADE)
	#
#
class MediaVilla(Media):
	photo = models.ImageField(upload_to='photos/Villa')
	idLocation = models.ForeignKey('Villa', on_delete=models.CASCADE)
	#
#
