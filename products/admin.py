from django.contrib import admin
from .models import Product, Category, CatEarColor, QuipuForm


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'sku',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class CatEarColorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class QuipuFormAdmin(admin.ModelAdmin):
    list_display = (
        'quipu_color',
        'quipu_stone_pearl',
        'name_field',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CatEarColor, CatEarColorAdmin)
admin.site.register(QuipuForm, QuipuFormAdmin)
