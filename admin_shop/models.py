from django.db import models


# Create your models here.
class Marque(models.Model):
    label_marque = models.CharField(max_length=250)

    def __str__(self):
        return self.label_marque


# classe produit
class Produit(models.Model):
    Taille = [
        ("L","L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
    ]
    label = models.CharField(max_length=250)
    Prices = models.FloatField(default=0.0)
    description = models.TextField(max_length=10000,blank=True)
    size = models.CharField(max_length=50,null=False ,blank=False, choices=Taille,default="L")# taille du podruit : L,XL,X
    quantity = models.PositiveIntegerField(default=0)
    date_add = models.DateTimeField(auto_now=True)
    marque= models.ForeignKey(Marque,on_delete=models.CASCADE)# clé referencielle
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)

    def __str__(self):
        return self.label

# classe panier
class Cart(models.Model):
    list_cart =models.ManyToManyField(Produit)


# classe preference
class WhistListCart(models.Model):
    prod = models.ManyToManyField(Produit)


class Country(models.Model):
    name_count = models.CharField(max_length=200)

    def __str__(self):
        return self.name_count


class City(models.Model):
    name_city = models.CharField(max_length=200)
    name_count = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_city

# classe profile de l'utilisateur
class Profile(models.Model):
    name = models.CharField(max_length=200)
    fistname = models.CharField(max_length=200)
    Address = models.CharField(max_length=250)
    name_count = models.ForeignKey(Country, on_delete=models.CASCADE)
    name_city = models.ForeignKey(City, on_delete=models.CASCADE)
    sexe = models.TextChoices("Masculin", "Feminin")
    # -> facebook_urls pas obligatoire
    # -> twitter_urls pas obligatoire
    # -> linkded_urls pas obligatoire
    def __str__(self):
        return self.name



