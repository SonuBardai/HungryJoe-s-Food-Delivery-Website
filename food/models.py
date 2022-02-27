from food.app import db

class Menu(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    img_loc = db.Column(db.String(25), nullable=False)

class Book(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(25), nullable=False)
    persons = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(15), nullable=False)