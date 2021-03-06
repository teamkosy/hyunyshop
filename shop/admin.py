from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category', 'price', 'stock', 'available_display', 'available_order', 'created', 'updated']
    list_flter = ['available_display', 'created', 'updated', 'category']
    prepopulated_field = {'slug':('name',)}
    list_editable = ['price', 'stock', 'available_display', 'available_order']
