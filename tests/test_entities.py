from springfield_mongo.entities import Entity as MongoEntity
from springfield_mongo import fields
from springfield_mongo import utils
import pytest
from bson.objectid import ObjectId
from bson.objectid import InvalidId


def test_mongo_entity():
    """
    Verify that a MongoEntity has the attributes and attribute types that we expect.
    """
    m = MongoEntity()

    i = ObjectId()
    m.id = i
    assert m.id == i

    with pytest.raises(InvalidId):
        m.id = 'monkey'
