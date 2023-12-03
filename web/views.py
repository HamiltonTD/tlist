from django.shortcuts import render
from django.db.models import Max
from .models import Item, Tag

def index(request):
    
    tag_list = Tag.objects.annotate(max_add_date=Max('item__add_date')).order_by('-max_add_date')

    tags_with_items = {}


    for tag in tag_list:
        
        items = Item.objects.filter(tag=tag).order_by('-add_date')
        items_with_tags = []
        
        for item in items:
        
            related_tags = item.tag.exclude(pk=tag.pk)
            items_with_tags.append({'item': item, 'related_tags': related_tags})

        tags_with_items[tag] = items_with_tags

    return render(request, 'web/index.html', {'tags_with_items': tags_with_items})
