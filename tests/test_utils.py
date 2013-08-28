from springfield_mongo import utils
from springfield_mongo.fields import ObjectIdField
from springfield import fields
from springfield import Entity
from bson.objectid import ObjectId


# This dummy class just used to have an extra attribute to verify during
# using the utils
class FooEntity(Entity):
    id = ObjectIdField()
    foo = fields.StringField()


def test_entity_to_mongo():
    i = ObjectId()
    m = FooEntity()
    m.id = i
    m.foo = 'monkey'

    mongo_document = utils.entity_to_mongo(m)
    assert '_id' in mongo_document
    assert mongo_document['_id'] == i
    assert 'foo' in mongo_document
    assert mongo_document['foo'] == 'monkey'


def test_entity_from_mongo():
    i = ObjectId()
    m = FooEntity()
    m.id = i
    m.foo = 'gorilla'

    mongo_document = utils.entity_to_mongo(m)
    entity = utils.entity_from_mongo(FooEntity, mongo_document)
    assert '_id' not in entity
    assert 'id' in entity
    assert entity['id'] == i
    assert 'foo' in entity
    assert entity['foo'] == 'gorilla'


def test_to_and_from_equality():
    i = ObjectId()
    m = FooEntity()
    m.id = i
    m.foo = 'giraffe'

    mongo_document = utils.entity_to_mongo(m)
    entity = utils.entity_from_mongo(FooEntity, mongo_document)
    assert m == entity
    mongo_document2 = utils.entity_to_mongo(entity)
    assert mongo_document2 == mongo_document
