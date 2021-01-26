from django.db import models
from django.utils.html import mark_safe
# Create your models here.

class ProductCategory(models.Model):

    prodcut_categ = models.CharField(max_length=50)
    product_categ_img = models.ImageField(upload_to="gallary/categ", null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.product_categ_img:
            print(self.product_categ_img.url)
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.product_categ_img.url))
        return ""

    def __str__(self):
        return self.prodcut_categ
    

class Product(models.Model):

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    product_categ_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_img = models.ImageField(upload_to="gallary", null=True, blank=True)
    
    @property
    def thumbnail_preview(self):
        if self.product_img:
            print(self.product_img.url)
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.product_img.url))

        return ""
        
    def __str__(self):
        ret = self.name

        return ret