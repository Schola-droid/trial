from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import func


db = SQLAlchemy()


# USER MODULE
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    promotion_id =db.Column(db.Integer, db.ForeignKey('promotions.id'))
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    role = db.Column(db.String)



    # Relationships
    customers = db.relationship('Customer', backref='users', uselist=False)
    shopowners = db.relationship('Shopowner', backref='users', uselist=False)
    riders = db.relationship('Rider', backref='users', uselist=False)
    profile_status = db.relationship('ProfileStatus', backref='users', uselist=False)
    admins = db.relationship('Admin', backref='users', uselist=False)
    super_admin = db.relationship('SuperAdmin', backref='users', uselist=False)
    carts = db.relationship('Cart',backref='users',uselist=True)
    product_reviews = db.relationship('ProductReview', backref='users', uselist=True)
    shop_reviews = db.relationship('ShopReview', backref='users', uselist=True)
    rider_reviews = db.relationship('RiderReview', backref='users', uselist=True)
    orders = db.relationship('Order', backref='users', uselist=True)
    deliveries = db.relationship('Delivery', backref='users', uselist=True)
    favorites = db.relationship('Favorite', backref='users', uselist=True)




    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'role': self.role
        }
    

class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    profile_picture = db.Column(db.String, unique=True) 
    gender = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'profile_picture':self.profile_picture,
            'gender': self.gender
        }
    
class SuperAdmin(db.Model):
    __tablename__ = 'super_admin'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    profile_picture = db.Column(db.String, unique=True) 
    gender = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'profile_picture':self.profile_picture,
            'gender': self.gender
        }

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, unique=True)
    last_name = db.Column(db.String, unique=True)
    profile_picture = db.Column(db.String, unique=True)
    location = db.Column(db.String)  
    gender = db.Column(db.String)  
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  

    def to_dict(self):
        return{
            'id': self.id,
            'first_name':self.first_name,
            'last_name': self.last_name,
            'profile_picture':self.profile_picture,
            'location':self.location,
            'gender': self.gender
        }

class Shopowner(db.Model):
    __tablename__ = 'shopowners'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, unique=True)
    last_name = db.Column(db.String, unique=True)
    profile_picture = db.Column(db.String, unique=True)
    location = db.Column(db.String)  
    gender = db.Column(db.String) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))   

    shops = db.relationship('Shop', backref='shopowners', uselist=True)

    def to_dict(self):
        return{   
            'id': self.id,         
            'first_name':self.first_name,
            'last_name': self.last_name ,
            'profile_picture': self.profile_picture,
            'location': self.location,
            'gender': self.gender
        }

class Rider(db.Model):
    __tablename__ = 'riders'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, unique=True)
    last_name = db.Column(db.String, unique=True)
    profile_picture = db.Column(db.String, unique=True)
    location = db.Column(db.String)  
    gender = db.Column(db.String)  
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  

    deliveries = db.relationship('Delivery', backref='riders', uselist=True)
    
    def to_dict(self):
        return{
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'profile_picture': self.profile_picture, 
            'location': self.location,
            'gender': self.gender
        }
    
        
 
class ProfileStatus(db.Model):
    __tablename__ = 'profile_status'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    deletion_date = db.Column(db.DateTime)
    

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'deletion_date': self.deletion_date
        }

class Promotion(db.Model):
    __tablename__ = 'promotions'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String)
    body = db.Column(db.String)
    creator = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    mailing_list = db.Column(db.String)  

    users = db.relationship('User', backref='promotions')

    def to_dict(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'body': self.body,
            'creator': self.creator,
            'created_at': self.created_at.strftime('%Y-%m-%d'),
            'mailing_list': self.mailing_list  
        }


    


# PRODUCTS MODULE

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    products = db.relationship('Product', backref='categories', uselist=True) 

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name
        }



class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))
    product_status = db.Column(db.String)
    price = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    
    images = db.relationship('Image', backref='products', uselist=True)
    cart = db.relationship('Cart', backref='products', uselist=True)
    favorites = db.relationship('Favorite', backref='products', uselist=True)


    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'product_status': self.product_status,
            'price': self.price
        }


    


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)  
    description = db.Column(db.String)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def to_dict(self):
        return{
            'id': self.id,
            'url': self.url,
            'description': self.description
        }

class Shop(db.Model):
    __tablename__ = 'shops'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    shopowners_id = db.Column(db.Integer, db.ForeignKey('shopowners.id'))


    products = db.relationship('Product', backref='shops', uselist=True)



    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'location': self.location
        }
    
    

# DELIVERIES MODULE
class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    product_id = db.Column(db.Integer, ForeignKey('products.id'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)

    # Relationships
    # users = db.relationship('User', backref='carts', uselist=True)

    def to_dict(self):
        return {
            'id': self.id,
            'quantity': self.quantity,
            'price': self.price
        }

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    order_date = db.Column(db.DateTime, default=func.now())
    delivery_id = db.Column(db.Integer, db.ForeignKey('deliveries.id'))


    products = db.relationship('Product', backref='orders', uselist=True)

    def to_dict(self):
        return{
            'id': self.id,
            'quantity': self.quantity,
            'order_date':self.order_date
        }
    
    




class Delivery(db.Model):
    __tablename__ = 'deliveries'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rider_id = db.Column(db.Integer, db.ForeignKey('riders.id')) 
    location = db.Column(db.String)
    payment_amount = db.Column(db.Integer)
    delivery_state = db.Column(db.String)
    dispatched = db.Column(db.String)

    orders = db.relationship('Order', backref='deliveries', uselist=True)

    def to_dict(self):
        return{
            'id': self.id,
            'location': self.location,
            'payment_amount': self.payment_amount,
            'delivery_state': self.delivery_state,
            'dispatched': self.dispatched
        }
    


# REVIEW MODULES

class ProductReview(db.Model):
    __tablename__ = 'product_reviews'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  
    comment = db.Column(db.String)
    rating = db.Column(db.String)

    def to_dict(self):
        return{
            'id': self.id,
            'rating': self.rating,
            'comment': self.comment
        }

class ShopReview(db.Model):
    __tablename__ = 'shop_reviews'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  
    comment = db.Column(db.String)
    rating = db.Column(db.String)

    def to_dict(self):
        return{
            'id': self.id,
            'rating': self.rating,
            'comment': self.comment
        }

class RiderReview(db.Model):
    __tablename__ = 'rider_reviews'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  
    comment = db.Column(db.String)
    rating = db.Column(db.String)

    def to_dict(self):
        return{
            'id': self.id,
            'rating': self.rating,
            'comment': self.comment
        }

class Favorite(db.Model):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_id': self.product_id
        }
    

# class Shop(db.Model):
#     __tablename__ = 'shops'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     location = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default = db.func.now())
#     updated_at = db.Column(db.DateTime, onupdate = db.func.now())
   

#     def to_dict(self):
#         return{
#             'id': self.id,
#             'name': self.name,
#             'location': self.location
#         }
    
#     shops_products = db.relationship("ShopsProducts", backref = "shops")

# class Product(db.Model):
#     __tablename__ = 'products'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     description = db.Column(db.String)
#     product_status = db.Column(db.String)
#     price = db.Column(db.Float)


#     def to_dict(self):
#         return{
#             'id': self.id,
#             'name': self.name,
#             'description': self.description,
#             'shop_id': self.shop_id,
#             'product_status': self.product_status,
#             'price': self.price
#         }
    
#     shops_products = db.relationship("ShopsProducts", backref = "products")
    
# class ShopsProducts(db.Model):
#     __tablename__ = 'shopsproducts'

#     id = db.Column(db.Integer, primary_key=True)
#     shops_id = db.Column(db.Integer, db.ForeignKey('shops.id'))
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
#     url = db.Column(db.String)
#     description = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default = db.func.now())
#     updated_at = db.Column(db.DateTime, onupdate = db.func.now())

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'url': self.url,
#             'description': self.description
#         }




