from .blueprint import product  # blueprint 파일에서 product 객체 import
# models폴더안 mongodb에서 conn_mongodb 객체 improt
from models.mongodb import conn_mongodb #models 폴더안 mongodb폴더에서 conn_mongodb 객체 import
from models.product import Product  # models폴더안 product에서 Product 객체 improt
# 다운받은 flask 에서 request와 render_template import
from flask import  request, render_template
# 현재시간 import
from datetime import datetime
import os

from werkzeug.utils import secure_filename

@product.route('/form')  # url 등록
def form():
    # flask에서 받은 render_template , web page연결
    return render_template('product_form.html')

# 상품등록 API


@product.route('/regist', methods=['POST'])
def regist():
    # 전달받은 상품 정보
    form_data = request.form
    print(f"form_data 정보입니다.  {form_data}")
    print(f"form_data 정보입니다.  {form_data['name']}")
    print(f"form_data 정보입니다.  {form_data['price']}")
    print(f"form_data 정보입니다.  {form_data['description']}")
             
    thumbnail_img = request.files.get('thumbnail_img')
    detail_img = request.files.get('detail_img')
    thumbnail_img_url=_upload_file(thumbnail_img)
    detail_img_url=_upload_file(detail_img)
    # 저장하는 일
    Product.insert_one(form_data,thumbnail_img_url,detail_img_url)

    return "상품 등록 API입니다"

#상품리스트 조회 API
@product.route('/list')
def get__products():
    #상품 리스트 정보 < mongo db products 컬렉션에 있는 documents
    products = Product.find()
    
    return render_template('products.html', products1 = products)



def _upload_file(img_file):
    timestamp = str(datetime.now().timestamp())
    filename = timestamp + '_' + secure_filename(img_file.filename)
    image_path=f'./static/uploads'
    os.makedirs(image_path, exist_ok=True)
    img = os.path.join(image_path, filename)
    img_file.save(img)
    
    return f'/static/uploads/' +filename
    
    