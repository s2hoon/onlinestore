from .mongodb import conn_mongodb

class Product():
    @staticmethod
    def insert_one(product):
        db = conn_mongodb()
        db.products.insert_one({
            'name': product['name'],
            'price': product['price'],
            'description' : product['description']
        })