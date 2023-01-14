import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://abhinav5600:<passwd>@cluster0.z5okehm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Abhinav",
    "surname": "Kumar",
    "email": "abhinav@gmail.com"
}

db1 = client['mongotest']
coll = db['test']
coll.insert_one(d)
