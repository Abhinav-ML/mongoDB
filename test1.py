import pymongo

client = pymongo.MongoClient("mongodb+srv://abhinav5600:abhik5600@cluster0.z5okehm.mongodb.net/?retryWrites=true&w=majority")
db =client.test

database = client['myinfo']
collection = db['user']

# record = collection.find()
# for i in record:
    # print(i)

# record = collection.find({'companyName': 'iNeuron' })
# for i in record:
#     print(i)

# record = collection.find({'courseOffered':'Machine Learning with Deployment' })
# for i in record:
#     print(i)

record = collection.find({'courseOffered': {"$gt":"E"} })
for i in record:
    print(i)