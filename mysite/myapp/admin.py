from django.contrib import admin

from .models import Product



admin.site.site_header = "Admin Panel"

admin.site.site_title = "Admin panel/phone shop"

admin.site.index_title = "Admin panel"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)
    list_editable = ('price','description')
    actions = ('make_zero',)

    def make_zero(self, request, queryset):
        queryset.update(price = 0)

admin.site.register(Product, ProductAdmin)

