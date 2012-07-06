from springfield.fields import AdaptableTypeField
from bson.objectid import ObjectId

class ObjectIdField(AdaptableTypeField):
    """
    TODO I don't like having a database specific field type in Springfield,
    but I haven't come up with a better alternative yet.
    """
    type = ObjectId

    def adapt(self, obj):
        try:
            return super(ObjectIdField, self).adapt(obj)
        except TypeError:
            if isinstance(obj, basestring):
                return ObjectId(obj)
            raise    

    def jsonify(self, value):
        """
        Get the value as a suitable JSON type
        """
        if value is not None:
            return str(value)