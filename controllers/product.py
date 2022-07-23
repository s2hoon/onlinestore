from .blueprint import product #blueprint 파일에서 product 객체 import
from models.mongodb import conn_mongodb #models폴더안 mongodb에서 conn_mongodb 객체 improt
from models.product import Product #models폴더안 product에서 Product 객체 improt


from flask import request ,render_template #다운받은 flask 에서 request와 render_template import




@product.route('/form') #url 등록
def form():
    return render_template('product_form.html') #flask에서 받은 render_template , web page연결


#상품등록 API
@product.route('/regist',methods=['POST'])
def regist():
    #전달받은 상품 정보
    form_data = request.form
    name = form_data['name']
    price = form_data['price']
    description = form_data['description']
    #저장하는 일
    Product.insert_one(form_data)
    
    return "상품 등록 API입니다"
