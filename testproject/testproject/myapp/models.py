from django.db import models

class Item(models.Model):
    name = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.name

class Subitem(models.Model):
    item = models.ForeignKey(Item, related_name = 'subitems')
    name = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.name