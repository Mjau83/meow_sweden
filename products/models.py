from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendley_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    catears_has_colors = models.BooleanField(default=False, null=True, blank=True)
    quipu_color = models.ForeignKey('Color', null=True, blank=True, on_delete=models.SET_NULL)
    quipu_stonepearl = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    hex_code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
