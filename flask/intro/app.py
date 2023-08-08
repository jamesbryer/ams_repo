from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/flask_test"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.sqlite  "
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI_INTRO')


db = SQLAlchemy(app)

# create a class for the table
class Person(db.Model):
    # create columns for the table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, default="John Doe")
    username = db.Column(db.String(50), nullable=False, unique=True)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    age = db.Column(db.Integer)

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False, default="John")
    last_name = db.Column(db.String(50), nullable=False, default="Doe")
    cars = db.relationship('Car', backref='ownerbr')

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num_plate = db.Column(db.String(50), nullable=False, default="ABC123")
    make = db.Column(db.String(50), nullable=False, default="Toyota")
    model = db.Column(db.String(50), nullable=False, default="Corolla")
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_number = db.Column(db.String(50), nullable=False, default="ABC123")
    products = db.relationship('Product', backref='orderbr')

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(50), nullable=False, default="ABC123")
    product_price = db.Column(db.Float, nullable=False, default=0.00)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)

class Order_Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

# can use a double decorator to add multiple routes to a function
@app.route("/")
@app.route("/home")
def home():
    return "Hello, Flask! You're the best!"

@app.route("/postoptions", methods=['GET', 'POST'])
def posto():
    #print(request.method)
    response = request.method
    return f"Method is {response}"

@app.route("/name/<word>")
def name(word):
    var1 = ("<h1 style='color: green'>" + word + "</h1>" + "<br/>") * 5
    return var1

# takes arguements for word and number of times to repeat
@app.route("/num/<word>/<int:num>")
def num(word, num):
    var1 = ("<h1 style='color: green'>" + word + "</h1>" + "<br/>") * num
    return var1

@app.route("/square/<int:num>")
def square(num):
    var1 = num ** 2
    return str(var1)

# redirects to google
@app.route("/redirect")
def redirecting():
    return redirect("https://www.google.com")

# using url_for to redirect to a function name instead of a url
@app.route("/gotohome")
def go_to_home():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
