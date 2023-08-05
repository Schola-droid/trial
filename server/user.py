from flask import Flask, make_response, jsonify, request, Blueprint
from flask_migrate import Migrate
from products import users_blueprint
from models import db, Customer, Shopowner, Rider, ProfileStatus, Promotion

#PART OF USERS CRUD
@users_blueprint.route('/customers', methods=['GET'])
def get_all_customers():
    customers = Customer.query.all()
    customer_list = []
    for customer in customers:
        customer_dict = {
            'id': customer.id,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'profile_picture': customer.profile_picture,
            'location': customer.location,
            'gender': customer.gender 
        }
        customer_list.append(customer_dict)
    response = make_response(
        jsonify(customer_list),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@users_blueprint.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer_by_id(customer_id):
    customer = Customer.query.filter_by(id=id).first()
    # if shop is None:
    #     return make_response(jsonify({'error': 'Shop not found'}), 404)
    customer_dict = {
            'id': customer.id,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'profile_picture': customer.profile_picture,
            'location': customer.location,
            'gender': customer.gender 
    }
    response = make_response(
        jsonify(customer_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@users_blueprint.route("/addcustomer", methods=["POST"])
def post_customer():
    data = request.get_json()
    new_customer = Customer(
        first_name=data["first_name"],
        last_name=data["last_name"],
        profile_picture=data["profile_picture"],
        location=data["location"],
        gender=data["gender"] 
    )
    db.session.add(new_customer)
    db.session.commit()
    response_message = {"message": "Customer added successfully"}
    return make_response(jsonify(response_message), 200)

@users_blueprint.route('/Customer/<int:customer_id>', methods=['PATCH'])
def update_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify(message='Customer not found'), 404
    
    updated_data = request.get_json()
    if not updated_data:
        return jsonify(message='Invalid or empty JSON data'), 400

    if 'first_name' in updated_data:
        customer.first_name = updated_data['first_name']
    if 'last_name' in updated_data:
        customer.last_name = updated_data['last_name']
    if 'profile_picture' in updated_data:
        customer.profile_picture = updated_data['profile_picture']
    if 'location' in updated_data:
        customer.location = updated_data['location']
    if 'gender' in updated_data:
        customer.gender = updated_data['gender']
    
    db.session.commit()
    return jsonify(message='Shop updated successfully')


@users_blueprint.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = Customer.query.filter_by(id = customer_id).first()
    if not customer:
        return jsonify({"message":'Customer not found'}), 404
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message":'Customer deleted successfully'})

#SHOPOWNER CRUD

@users_blueprint.route('/shopowners', methods=['GET'])
def get_all_shopowners():
    shopowners = Shopowner.query.all()
    shopowner_list = []
    for shopowner in shopowners:
        shopowner_dict = {
            'id': shopowner.id,
            'first_name': shopowner.first_name,
            'last_name': shopowner.last_name,
            'profile_picture': shopowner.profile_picture,
            'location': shopowner.location,
            'gender': shopowner.gender 
        }
        shopowner_list.append(shopowner_dict)
    response = make_response(
        jsonify(shopowner_list),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@users_blueprint.route('/shopowners/<int:shopowner_id>', methods=['GET'])
def get_shopowner_by_id(shopowner_id):
    shopowner = Shopowner.query.filter_by(id=id).first()
    # if shop is None:
    #     return make_response(jsonify({'error': 'Shop not found'}), 404)
    shopowner_dict = {
            'id': shopowner.id,
            'first_name': shopowner.first_name,
            'last_name': shopowner.last_name,
            'profile_picture': shopowner.profile_picture,
            'location': shopowner.location,
            'gender': shopowner.gender 
    }
    response = make_response(
        jsonify(shopowner_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@users_blueprint.route("/addshopowner", methods=["POST"])
def post_shopowner():
    data = request.get_json()
    new_shopowner = Shopowner(
        first_name=data["first_name"],
        last_name=data["last_name"],
        profile_picture=data["profile_picture"],
        location=data["location"],
        gender=data["gender"] 
    )
    db.session.add(new_shopowner)
    db.session.commit()
    response_message = {"message": "Shopowner added successfully"}
    return make_response(jsonify(response_message), 200)

@users_blueprint.route('/Shopowner/<int:shopowner_id>', methods=['PATCH'])
def update_shopowner(shopowner_id):
    shopowner = Shopowner.query.get(shopowner_id)
    if not shopowner:
        return jsonify(message='Shopowner not found'), 404
    
    updated_data = request.get_json()
    if not updated_data:
        return jsonify(message='Invalid or empty JSON data'), 400

    if 'first_name' in updated_data:
        shopowner.first_name = updated_data['first_name']
    if 'last_name' in updated_data:
        shopowner.last_name = updated_data['last_name']
    if 'profile_picture' in updated_data:
        shopowner.profile_picture = updated_data['profile_picture']
    if 'location' in updated_data:
        shopowner.location = updated_data['location']
    if 'gender' in updated_data:
        shopowner.gender = updated_data['gender']
    
    db.session.commit()
    return jsonify(message='Shopowner updated successfully')


@users_blueprint.route('/shopowner/<int:shopowner_id>', methods=['DELETE'])
def delete_shopwowner(shopowner_id):
    shopowner = Shopowner.query.filter_by(id = shopowner_id).first()
    if not shopowner:
        return jsonify({"message":'Shopowner not found'}), 404
    db.session.delete(shopowner)
    db.session.commit()
    return jsonify({"message":'Shopowner deleted successfully'})

#RIDER CRUD

@users_blueprint.route('/riders', methods=['GET'])
def get_all_riders():
    riders = Rider.query.all()
    rider_list = []
    for rider in riders:
        rider_dict = {
            'id': rider.id,
            'first_name': rider.first_name,
            'last_name': rider.last_name,
            'profile_picture': rider.profile_picture,
            'location': rider.location,
            'gender': rider.gender 
        }
        rider_list.append(rider_dict)
    response = make_response(
        jsonify(rider_list),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@users_blueprint.route('/riders/<int:rider_id>', methods=['GET'])
def get_rider_by_id(rider_id):
    rider = Rider.query.filter_by(id=id).first()
    # if shop is None:
    #     return make_response(jsonify({'error': 'Shop not found'}), 404)
    rider_dict = {
            'id': rider.id,
            'first_name': rider.first_name,
            'last_name': rider.last_name,
            'profile_picture': rider.profile_picture,
            'location': rider.location,
            'gender': rider.gender 
    }
    response = make_response(
        jsonify(rider_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@users_blueprint.route("/addrider", methods=["POST"])
def post_rider():
    data = request.get_json()
    new_rider = Rider(
        first_name=data["first_name"],
        last_name=data["last_name"],
        profile_picture=data["profile_picture"],
        location=data["location"],
        gender=data["gender"] 
    )
    db.session.add(new_rider)
    db.session.commit()
    response_message = {"message": "Rider added successfully"}
    return make_response(jsonify(response_message), 200)

@users_blueprint.route('/rider/<int:rider_id>', methods=['PATCH'])
def update_rider(rider_id):
    rider = Rider.query.get(rider_id)
    if not rider:
        return jsonify(message='Rider not found'), 404
    
    updated_data = request.get_json()
    if not updated_data:
        return jsonify(message='Invalid or empty JSON data'), 400

    if 'first_name' in updated_data:
        rider.first_name = updated_data['first_name']
    if 'last_name' in updated_data:
        rider.last_name = updated_data['last_name']
    if 'profile_picture' in updated_data:
        rider.profile_picture = updated_data['profile_picture']
    if 'location' in updated_data:
        rider.location = updated_data['location']
    if 'gender' in updated_data:
        rider.gender = updated_data['gender']
    
    db.session.commit()
    return jsonify(message='Rider updated successfully')


@users_blueprint.route('/rider/<int:rider_id>', methods=['DELETE'])
def delete_rider(rider_id):
    rider = Rider.query.filter_by(id = rider_id).first()
    if not rider:
        return jsonify({"message":'Rider not found'}), 404
    db.session.delete(rider)
    db.session.commit()
    return jsonify({"message":'Rider deleted successfully'})

