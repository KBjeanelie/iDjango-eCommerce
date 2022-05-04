from django.db import models


# Create your models here.
class Marque(models.Model):
    label_marque = models.CharField(max_length=250)


# classe produit
class Produit(models.Model):
    Taille = (
        ("L","L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
    )
    label = models.CharField(max_length=250)
    Prices = models.FloatField()
    description = models.TextField(max_length=10000)
    size = models.CharField(max_length=50, null=False, choices=Taille)# taille du podruit : L,XL,X
    quantity = models.PositiveIntegerField()
    #label= models.ForeignKey(Marque, on_delete=models.CASCADE)# clé referencielle
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)

# classe panier
class Cart(models.Model):
    list_cart =[] # a revoire

    def add_product(self, Produit):
        self.list_cart.append(Produit)

    def remove_product(self, Produit):
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

class City(models.Model):
    name_city = models.CharField(max_length=200)


class Country(models.Model):
    name_count = models.CharField(max_length=200)
    city_of_count = models.ForeignKey(City, on_delete=models.CASCADE)
# classe profile de l'utilisateur
class Profile(models.Model):
    Sexe_choix = (
        ("max", "Masculin"),
        ("fem", "Feminin"),
    )  # variable contenant le choix du sexe
    Address = models.CharField(max_length=250, null=False)
    #Country = models.CharField(max_length=200, choices=tuple(Country.name_count))
    #City = models.CharField(max_length=200, choices=City.name_city)
    sexe = models.CharField(max_length=100, null=False, choices=Sexe_choix)
    # -> facebook_urls pas obligatoire
    # -> twitter_urls pas obligatoire
    # -> linkded_urls pas obligatoire


