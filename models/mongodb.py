import pymongo


MONGO_URI = "mongodb+srv://s2hoon:FNlTVZlrLH7mN46S@cluster0.fnwwxb4.mongodb.net/?retryWrites=true&w=majority"
MONGO_CONN = pymongo.MongoClient(MONGO_URI)

def conn_mongodb():
    db = MONGO_CONN.online_store
    test_connection = db.test_connection.insert_one({'test':'test'})
    return db

conn_mongodb()