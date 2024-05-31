from django.contrib import admin
from .models import Product, Variation

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description_short', 'get_price_formated', 'get_price_promotional_formated']
    inlines = [
        VariationInline
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
