from springfield_mongo import fields
from springfield import Entity
import pytest
from bson.objectid import ObjectId
from bson.objectid import InvalidId

def test_objectid():
    class MongoEntity(Entity):
        _id = fields.ObjectIdField()

    e = MongoEntity()
    assert e._id is None

    with pytest.raises(InvalidId):
        # TODO Should adapters always raise a TypeError or is application specific errors ok?
        e._id = '1234'

    object_id = ObjectId()
    e._id = object_id

    assert e.jsonify()['_id'] == str(object_id)

    e._id = '4ff69dacc3e3f882f3000000'

    assert e._id == ObjectId('4ff69dacc3e3f882f3000000')

    assert MongoEntity(**e.jsonify())._id == ObjectId('4ff69dacc3e3f882f3000000')