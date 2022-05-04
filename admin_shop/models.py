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
    label = models.CharField(max_length=250,default="")
    Prices = models.FloatField(default=0.0)
    description = models.TextField(max_length=10000,blank=True)
    size = models.CharField(max_length=50,null=False ,blank=False, choices=Taille,default="L")# taille du podruit : L,XL,X
    quantity = models.PositiveIntegerField(default=0)
    marque= models.ForeignKey(Marque,on_delete=models.CASCADE,default="inconnu")# clé referencielle
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)

    def __str__(self):
        return self.label

# classe panier
class Cart(models.Model):
    list_cart =[] # a revoire

    def add_product(self, a):
        self.list_cart.append(Produit)

    def remove_product(self, a):
        self.list_cart.remove(Produit)


# classe preference
class WhistListCart(models.Model):
    prod = []
    # produits relation plusieur à plusieur avec la table produit
    # methode
    def add_product(self, a):
        self.prod.append(a)  # prend un produit en paramettre

    def remove_product(self,a):
        self.prod.remove(a) # prend un produit en paramettre

    def remove_all_product(self):
        self.prod.clear()

    def add_product_to_cart(self):
        pass


class Country(models.Model):
    name_count = models.CharField(max_length=200)

    def __str__(self):
        return self.name_count


class City(models.Model):
    name_city = models.CharField(max_length=200)
    city_of_count = models.ForeignKey(Country, on_delete=models.CASCADE,default="inconnu")

    def __str__(self):
        return self.name_city

# classe profile de l'utilisateur
class Profile(models.Model):
    name = models.CharField(max_length=200,blank=False,default="")
    fistname = models.CharField(max_length=200,blank=False,default="")
    Address = models.CharField(max_length=250, blank=False)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE,default="inconnu")
    #City_of_profile = models.CharField(City, on_delete=models.CASCADE)
    sexe = models.TextChoices("Masculin", "Feminin")
    # -> facebook_urls pas obligatoire
    # -> twitter_urls pas obligatoire
    # -> linkded_urls pas obligatoire
    def __str__(self):
        return self.name + self.fistname



