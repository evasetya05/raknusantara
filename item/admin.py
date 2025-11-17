from django.contrib import admin
from .models import Category, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')
    search_fields = ('id', 'name', 'category', 'description')
    ordering = ('id',)
    list_filter = ('category',)


admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
