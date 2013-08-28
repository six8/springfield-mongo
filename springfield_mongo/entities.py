from springfield import Entity as BaseEntity
from springfield_mongo.fields import ObjectIdField


class Entity(BaseEntity):
    id = ObjectIdField()
