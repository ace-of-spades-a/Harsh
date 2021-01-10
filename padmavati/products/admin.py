from django.contrib import admin
from .models import Product, ProductCategory 
# Register your models here.

# admin.site.register(Product)
# admin.site.register(ProductCategory)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'product_categ_id', 'product_img']
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Product Image'
    thumbnail_preview.allow_tags = True

admin.site.register(Product, ProductAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['prodcut_categ', 'product_categ_img']
    readonly_fields = ('thumbnail_preview',)
    
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Category Image'
    thumbnail_preview.allow_tags = True

admin.site.register(ProductCategory, ProductCategoryAdmin)