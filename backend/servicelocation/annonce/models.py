from django.contrib.gis.db import models

class Location(models.Model):
    bailleur_id = models.IntegerField(null=True)  # Utiliser l'ID du bailleur existant
    typeLocation = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    location = models.PointField(null=True)

    def __str__(self):
        return f"{self.type} in {self.city}"

class Characteristic(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='characteristics')
    name = models.CharField(max_length=50, null=True)
    count = models.IntegerField(null=True)
    image = models.ImageField(upload_to='characteristics/')

    def __str__(self):
        return self.name

