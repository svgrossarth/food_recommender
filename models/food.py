from mongoengine import Document, StringField, DateTimeField, EmbeddedDocument, EmbeddedDocumentField, ListField, UUIDField
import uuid
from datetime import datetime

class Column(EmbeddedDocument):
    col_name = StringField(required=True)
    value = StringField()

class FoodItem(Document):
    food_id = UUIDField(default=uuid.uuid4, unique=True, required=True)
    user_id = UUIDField(required=True)
    name = StringField(required=True)
    date_created = DateTimeField(default=datetime.now)
    date_updated = DateTimeField(default=datetime.now)
    columns = ListField(EmbeddedDocumentField(Column), required=True)

    def __init__(self, *args, **kwargs):
        super(FoodItem, self).__init__(*args, **kwargs)
        self.date_created = datetime.now()
        self.date_updated = datetime.now()

# lets look at this more
    def save(self, *args, **kwargs):
        return super(FoodItem, self).save(*args, **kwargs)


    def update(self, *args, **kwargs):
        self.date_updated = datetime.now() 
        return super(FoodItem, self).save(*args, **kwargs)

