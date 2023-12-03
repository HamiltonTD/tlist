from django.db import models


##-------------------------------------------------------------------------------------->> 
## tag
##--------------------------------------------------------------------------------------<<
class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
            return self.name
        

##-------------------------------------------------------------------------------------->> 
## item
##--------------------------------------------------------------------------------------<<
class Item(models.Model):
    
    FAVORITE_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]
    
    name= models.CharField(max_length=255)
    link= models.CharField(max_length=255, blank=True)
    favorite = models.BooleanField(choices=FAVORITE_CHOICES, default=False)
    summary = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True) 
    add_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
