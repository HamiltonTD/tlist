from django.contrib import admin
from .models import Item, Tag


##-------------------------------------------------------------------------------------->> 
## tag
##--------------------------------------------------------------------------------------<<
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
    search_fields = ('name', 'name')
    
    
##-------------------------------------------------------------------------------------->> 
## item
##--------------------------------------------------------------------------------------<<
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'add_date', 'favorite')
    search_fields = ('name', 'link')