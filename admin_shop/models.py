from django.db import models

# Create your models here.
class Marque(models.Model):
    label_marque = models.CharField(max_length=250)

    def __str__(self):
        return self.label_marque
#classe categorie
class Categorie(models.Model):
    label_Categorie = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.label_Categorie
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
    marque = models.ForeignKey(Marque,on_delete=models.CASCADE)# clé referencielle
    label_Categorie= models.ForeignKey(Categorie,on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(blank=True,upload_to='images')
    image3 = models.ImageField(blank=True,upload_to='images')

    def __str__(self):
        return self.label

# classe panier
class Cart(models.Model):
    list_cart =models.ManyToManyField(Produit)
    Total_frais = models.PositiveBigIntegerField(default=0)


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
    facebook_urls = models.URLField(blank=True)
    twitter_urls = models.URLField(blank=True)
    linkded_urls = models.URLField(blank=True)

    def __str__(self):
        return self.name



