from flask import Flask, make_response, jsonify, request, Blueprint
from flask_migrate import Migrate
from products import products_blueprint


from models import db, Shop, Product, Category, Image



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbspeedy_user:u5WodHoXeyVOEjUcNhIMdtBJUIgc1Sx2@dpg-cj4frmt9aq047ccf6egg-a.oregon-postgres.render.com/dbspeedy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
app.register_blueprint(products_blueprint)


migrate = Migrate(app, db)


db.init_app(app)



if __name__ == '__main__':
    app.run(port=5555)
