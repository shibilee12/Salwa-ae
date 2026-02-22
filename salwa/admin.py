from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'business_type', 'price', 'is_featured')
    list_filter = ('business_type',)
    search_fields = ('title',)
