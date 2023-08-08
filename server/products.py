from flask import Blueprint,make_response, jsonify, request
from models import db, Shop, Product, Category, Image


#SHOP CRUD
products_blueprint = Blueprint('products', __name__)

@products_blueprint.route('/shops', methods=['GET'])
def get_all_shops():
    shops = Shop.query.all()
    shop_list = []
    for shop in shops:
        shop_dict = {
            'id': shop.id,
            'name': shop.name,
            'location': shop.location
        }
        shop_list.append(shop_dict)
    response = make_response(
        jsonify(shop_list),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@products_blueprint.route('/shops/<int:id>')
def get_shop_by_id(id):
    shop = Shop.query.filter_by(id=id).first()
    if shop is None:
        response = make_response(jsonify({'error': 'Shop not found'}), 404)
    else:
        shop_dict = {
            'id': shop.id,
            'name': shop.name,
            'location': shop.location
        }
        
        response = make_response(jsonify(shop_dict), 200)
    response.headers["Content-Type"] = "application/json"

    return response

@products_blueprint.route("/addshop", methods=["POST"])
def post_shop():
    data = request.get_json()
    new_shop = Shop(
        name=data["name"],
        location=data["location"]
    )
    db.session.add(new_shop)
    db.session.commit()
    response_message = {"message": "Shop added successfully"}
    return make_response(jsonify(response_message), 200)

@products_blueprint.route('/shop/<int:shop_id>', methods=['PATCH'])
def update_shop(shop_id):
    shop = Shop.query.get(shop_id)
    if not shop:
        return jsonify(message='Shop not found'), 404
    
    updated_data = request.get_json()
    if not updated_data:
        return jsonify(message='Invalid or empty JSON data'), 400

    if 'name' in updated_data:
        shop.name = updated_data['name']
    if 'location' in updated_data:
        shop.location = updated_data['location']
    
    db.session.commit()
    return jsonify(message='Shop updated successfully')


@products_blueprint.route('/shop/<int:shop_id>', methods=['DELETE'])
def delete_shop(shop_id):
    shop = Shop.query.filter_by(id = shop_id).first()
    if not shop:
        return jsonify({"message":'Shop not found'}), 404
    db.session.delete(shop)
    db.session.commit()
    return jsonify({"message":'Shop deleted successfully'})


# #PRODUCTS CRUD

@products_blueprint.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_dict = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'product_status': product.status,
            'price': product.price
        }
        product_list.append(product_dict)
    response = make_response(
        jsonify(product_list),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@products_blueprint.route('/products/<int:id>')
def get_product_by_id(id):
    product = Product.query.filter_by(id=id).first()
    if product is None:
        response = make_response(jsonify({'error': 'Product not found'}), 404)
    else:
        product_dict = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'product_status': product.status,
        'price': product.price
        }

        response = make_response(jsonify(product_dict), 200)
    response.headers["Content-Type"] = "application/json"

    return response
    

@products_blueprint.route("/addproduct", methods=["POST"])
def post_product():
    data = request.get_json()
    new_product = Product(
        name=data["name"],
        description=data["description"],
        product_status=data["product_status"],
        price=data["data"]
    )
    db.session.add(new_product)
    db.session.commit()
    response_message = {"message": "Product added successfully"}
    return make_response(jsonify(response_message), 200)


@products_blueprint.route('/product/<int:product_id>', methods=['PATCH'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify(message='Product not found'), 404
    
    updated_data = request.get_json()
    if not updated_data:
        return jsonify(message='Invalid or empty JSON data'), 400

    if 'name' in updated_data:
        product.name = updated_data['name']
    if 'description' in updated_data:
        product.description = updated_data['description']
    if 'product_status' in updated_data:
        product.product_status = updated_data['product_status']
    if 'price' in updated_data:
        product.price = updated_data['price']
    
    db.session.commit()
    return jsonify(message='Product updated successfully')


@products_blueprint.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.filter_by(id = product_id).first()
    if not product:
        return jsonify({"message":'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message":'Product deleted successfully'})

#CATEGORY CRUD

@products_blueprint.route('/categories', methods=['GET'])
def get_all_categories():
    categories = Category.query.all()
    category_list = []
    for category in categories:
        category_dict = {
            'id': category.id,
            'name': category.name
        }
        category_list.append(category_dict)
    response = make_response(
        jsonify(category_list),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@products_blueprint.route('/categories/<int:id>')
def get_category_by_id(id):
    category = Category.query.filter_by(id=id).first()
    if category is None:
        response = make_response(jsonify({'error': 'Category not found'}), 404)
    else:
        category_dict = {
            'id': category.id,
            'name': category.name
        }
        
        response = make_response(jsonify(category_dict), 200)
    response.headers["Content-Type"] = "application/json"

    return response

@products_blueprint.route("/addcategory", methods=["POST"])
def post_category():
    data = request.get_json()
    new_category = Category(
        name=data["name"]
    )
    db.session.add(new_category)
    db.session.commit()
    response_message = {"message": "Category added successfully"}
    return make_response(jsonify(response_message), 200)

@products_blueprint.route('/category/<int:product_id>', methods=['PATCH'])
def update_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify(message='Category not found'), 404
    
    updated_data = request.get_json()
    if not updated_data:
        return jsonify(message='Invalid or empty JSON data'), 400

    if 'name' in updated_data:
        category.name = updated_data['name']
    
    db.session.commit()
    return jsonify(message='Category updated successfully')


@products_blueprint.route('/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.filter_by(id = category_id).first()
    if not category:
        return jsonify({"message":'Category not found'}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message":'Category deleted successfully'})

#IMAGE CRUD

@products_blueprint.route('/images', methods=['GET'])
def get_all_images():
    images = Image.query.all()
    image_list = []
    for image in images:
        image_dict = {
            'id': image.id,
            'url': image.url,
            'description': image.description
        }
        image_list.append(image_dict)
    response = make_response(
        jsonify(image_list),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@products_blueprint.route('/images/<int:id>')
def get_image_by_id(id):
    image = Image.query.filter_by(id=id).first()
    if image is None:
        response = make_response(jsonify({'error': 'Image not found'}), 404)
    else:
        image_dict = {
            'id': image.id,
            'url': image.url,
            'description': image.description
        }
        
        response = make_response(jsonify(image_dict), 200)
    response.headers["Content-Type"] = "application/json"

    return response

@products_blueprint.route("/addimage", methods=["POST"])
def post_image():
    data = request.get_json()
    new_image = Image(
        url=data["url"],
        description=data["description"]
    )
    db.session.add(new_image)
    db.session.commit()
    response_message = {"message": "Image added successfully"}
    return make_response(jsonify(response_message), 200)

@products_blueprint.route('/image/<int:image_id>', methods=['PATCH'])
def update_image(image_id):
    image = Image.query.get(image_id)
    if not image:
        return jsonify(message='Image not found'), 404
    
    updated_data = request.get_json()
    if not updated_data:
        return jsonify(message='Invalid or empty JSON data'), 400

    if 'url' in updated_data:
        image.url = updated_data['url']
    if 'description' in updated_data:
        image.description = updated_data['description']
    
    db.session.commit()
    return jsonify(message='Image updated successfully')


@products_blueprint.route('/image/<int:image_id>', methods=['DELETE'])
def delete_image(image_id):
    image = Image.query.filter_by(id = image_id).first()
    if not image:
        return jsonify({"message":'Image not found'}), 404
    db.session.delete(image)
    db.session.commit()
    return jsonify({"message":'Image deleted successfully'})
