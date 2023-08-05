from faker import Faker
from models import Shop, db, Product
from app import app
fake = Faker()
with app.app_context():
    Shop.query.delete()
    # Shops.query.delete()
    products = []
    for i in range(10):
        prdts = Product(name = fake.name(), description = fake.text(), product_status = fake.random_element(elements=('In stock', 'Out of stock')), price = fake.pyfloat(min_value=0, max_value=1000, right_digits=2))
        products.append(prdts)
    shops = []
    for i in range(10):
        shps = Shop(name = fake.name(), location = fake.city())
        shops.append(shps)
    # db.session.add_all(products)
    db.session.add_all(products)
    db.session.commit()
    db.session.add_all(shops)
    db.session.commit()
    
