from flask import Flask, render_template


# Create a flask instance
app = Flask(__name__)

@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"

def index():
    first_name = 'Edaurdo'
    stuff = "This is <strong>stuff</strong>"
    favorite_pizza = ['Pepperoni', 'Veggies', 'Hawaiian', 41]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)


@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)

# Custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500