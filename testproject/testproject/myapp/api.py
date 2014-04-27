from bambu_api import ModelAPI, ModelInline, site
from testproject.myapp.models import Item, Subitem

class SubitemInline(ModelInline):
    model = Subitem
    
    def example_object(self):
        return {
            'id': 1,
            'name': 'Example subitem',
            'item': 1
        }
        
class ItemAPI(ModelAPI):
    inlines = [SubitemInline]
    def example_object(self):
        return {
            'id': 1,
            'name': 'Example item'
        }

site.register(Item, ItemAPI)