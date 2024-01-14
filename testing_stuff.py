from pymongo import MongoClient

# Connection URL
# Assuming MongoDB is running on the default port 27017
client = MongoClient("mongodb://localhost:27017/")

# Specify the database to be used
db = client.test_database

# Specify the collection to be used
collection = db.test_collection

# Insert a document into the collection
post = {"author": "John", "text": "My first blog post!"}
post_id = collection.insert_one(post).inserted_id

# Retrieve the inserted document
retrieved_post = collection.find_one({"author": "John"})
print(f'spencer we got the goods from teh db: {retrieved_post}')
