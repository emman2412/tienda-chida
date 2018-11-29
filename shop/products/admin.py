from django.contrib import admin
from .models import Category, Product, Trademark
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class TrademarkAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Trademark, TrademarkAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'trademark', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    readonly_fields= ('created',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name','trademarks')
    class Media:
        css = {
            'all': ('products/css/custom_ckeditor.css',)
        }
        


admin.site.register(Product, ProductAdmin)