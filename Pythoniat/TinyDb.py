from tinydb import TinyDB , Query

db=TinyDB('julia.json')
#db.insert({"name" : "fati" , "job" : "CEO"})
ju = db.all()
#print(ju)
for item in db :
    print(item)

q = Query()

d = db.search(q.name  == "fati" )
print(d)
