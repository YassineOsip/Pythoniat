import couchdb

#start the couch server by runing this command  :  net start "apache couchdb"
couchserver = couchdb.Server()
dbname = "julia"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)

#del couchserver[dbname]
#doc_id, doc_rev = db.save({'name': 'julia'  , "job": "assistant"})
#doc = db["my_document_id"] = {'name': 'julia'}
#db.save(doc)
#doc = db["id"] = {'name': 'yassine'}
#db.save(doc)
db_id = "my_document_id"
d = db[db_id]
dd= db.get(db_id)
print(dd)