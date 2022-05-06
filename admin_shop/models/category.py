from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# classe categories
class Category(models.Model):
    label_category = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to='category_pics')
    slug = models.SlugField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('label_category',)
        ordering = ('-created_date',)

    def __str__(self):
        return self.label_category

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label_category)
        super(Category, self).save(*args, **kwargs)

    def get_absolut_url(self):
        return reverse('shop:category_view', kwargs={'slug': self.slug})
