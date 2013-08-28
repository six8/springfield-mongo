from springfield import Entity


def entity_from_mongo(cls, values):
    """
    Construct an Entity of type `cls` from a Mongo document.
    """
    entity = cls()
    if hasattr(values, '__values__'):
        for key, val in values.__values__.items():
            if key == '_id':
                key = 'id'

            if key in entity.__fields__:
                entity.set(key, val)
    else:
        for key, val in values.items():
            if key == '_id':
                key = 'id'

            if key in entity.__fields__:
                entity.set(key, val)
    return entity


def entity_to_mongo(entity):
    """
    Convert an Entity type into a structure able to be stored in Mongo.
    """
    data = {}
    for key, val in entity.__values__.iteritems():
        field = entity.__fields__[key]

        if isinstance(val, Entity):
            val = entity_to_mongo(val)
        else:
            val = field.flatten(val)

        if key == 'id':
            key = '_id'

        data[key] = val

    return data
