import pymongo

from pymongo import MongoClient

#connect to DB
connection=MongoClient('localhost',27017)

db=connection.test

names=db.names
val=names.find_one()

print val['name']

#Update name in DB

#var j=db.names.findOne()
#j.name="UpdatedName"
#db.names.save(j)
#db.names.find()