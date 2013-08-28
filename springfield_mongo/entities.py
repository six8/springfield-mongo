from springfield import Entity as BaseEntity
from springfield_mongo.fields import ObjectIdField


class Entity(BaseEntity):
    id = ObjectIdField()

    def __setitem__(self, key, value):
        # Handle mongo trying to set _id
        if key == '_id':
            key = 'id'
        return super(Entity, self).__setitem__(key, value)

    def __setattr__(self, key, value):
        # make sure to behave the same as __setitem__
        if key == '_id':
            key = 'id'
        return super(Entity, self).__setattr__(key, value)
