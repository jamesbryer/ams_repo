from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/world"
#database_uri = 'mysql+pymysql://root:root@localhost:8888/routes'

db = SQLAlchemy(app)

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
