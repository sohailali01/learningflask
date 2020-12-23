from flask import Flask
import flask
from flask import request, jsonify

from home import home_bp
from contact import contact_bp

app = Flask(__name__)

# @app.route('/hello/', methods=['GET', 'POST'])
# @app.route('/<int:number>/')
# def incrementer(number):
#     return "Incremented number is " + str(number + 1)
#
#
# @app.route('/<string:name>/')
# def hello(name):
#     return "Hello " + name


# @app.route('/person/')
# def hello():
#     return jsonify({'name': 'Sohail', 'address': 'Pakistan'})
#
#
# @app.route('/numbers/')
# def print_list():
#     return jsonify(list(range(5)))

# @app.route('/home/')
# def home():
#     return "Home page"
#
#
# @app.route('/contact')
# def contact():
#     return "Contact page"
#
#
# @app.route('/teapot/')
# def teapot():
#     return "Would you like some tea?", 418


# @app.before_request
# def before():
#     print("This is executed BEFORE each request.")
#
#
#  @app.route('/hello/')
# def hello():
#     return "Hello World!"


# app.register_blueprint(home_bp, url_prefix='/home')
# app.register_blueprint(contact_bp, url_prefix='/contact')
#
# app.run()
# # if __name__ == '__main__':
# #     app.run(host='127.0.0.1', port=3000)
#
# import flask
#
# app = flask.Flask(__name__)
# app.config["DEBUG"] = True
#
#
# @app.route('/home')
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
#
#
# app.run()

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()
