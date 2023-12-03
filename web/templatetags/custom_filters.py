from django import template
from django.utils.text import slugify as django_slugify

register = template.Library()


    
##-------------------------------------------------------------------------------------->> 
## replace dash '-' with dot '.'  
##--------------------------------------------------------------------------------------<<
@register.filter(name='slugify_dot')
def slugify_dot(value):
    return django_slugify(value).replace('-', '.')


##-------------------------------------------------------------------------------------->> 
## remove spaces  
##--------------------------------------------------------------------------------------<<
@register.filter(name='remove_spaces')
def remove_spaces(value):
    return value.replace(" ", "")