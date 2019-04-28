from django.contrib import admin
from .models import Item, Review, Tag

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    item_display = ['id', 'name', 'short_desc', 'photo',
                    'updated', 'tagged']
    item_display_links = ['id', 'name']
    list_filter = ['created_at', 'updated_at', 'tags', ]
    search_fields = ['name', 'desc', ]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'item', 'message', 'updated', ]
    list_display_links = ['id', 'message', ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_display_links = ['id', 'name', ]