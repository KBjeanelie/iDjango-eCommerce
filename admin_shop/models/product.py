from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from admin_shop.models.category import Category
from admin_shop.models.marque import Marque


class Product(models.Model):
    Taille = [
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
    ]

    label = models.CharField(max_length=250)

    slug = models.SlugField()

    prices = models.FloatField(default=0.0)

    description = models.TextField(max_length=1000, blank=True)

    size = models.CharField(max_length=50, null=False, blank=False, choices=Taille, default="L")

    quantity = models.PositiveIntegerField(default=0)

    date_add = models.DateTimeField(auto_now=True)

    update_on = models.DateTimeField(auto_now=True)

    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    image1 = models.ImageField(upload_to='product_img')

    image2 = models.ImageField(blank=True, upload_to='product_img')

    image3 = models.ImageField(blank=True, upload_to='product_img')

    def __str__(self):
        return self.label

    class Meta:
        unique_together = ("label",)
        ordering = ('-date_add',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)

    def get_absolut_url(self):
        return reverse('library:product_detail', kwargs={'slug': self.slug})

