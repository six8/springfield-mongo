from springfield_mongo.entities import Entity as MongoEntity
from springfield_mongo import fields
from springfield_mongo import utils
from bson.objectid import ObjectId


def test_mongo_entity():
    m = MongoEntity()

    m.id = ObjectId()

    # verify that when converting to json, the 'id' key is preserved.
    m_json = m.jsonify()
    assert 'id' in m_json

    # ...but verify that when converting to a mongo document, the id is 
    # translated.
    m_mongo = utils.entity_to_mongo(m)
    assert '_id' in m_mongo

    # verify that 'something' trying to set the invalid '_id' key will be
    # translated into the 'id' field.
    i = ObjectId()
    m['_id'] = i
    assert not hasattr(m, '_id')
    assert m.id == i

    # verify that __setattr__ behaves the same as __setitem__ with regard
    # to the translated '_id' key.
    j = ObjectId()
    m._id = j
    assert not hasattr(m, '_id')
    assert m.id == j
