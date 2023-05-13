from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from Resources import UserRegister, UserLogin, SearchRecipe, SuggestRecipe, RandomRecipe

"""
This module defines a Flask application that provides a RESTful API for fetching recipe information.

Endpoints:
- '/register': Allows users to register by sending a POST request with a JSON object containing their username and password. The endpoint returns a JSON object with a message indicating whether the registration was successful or not.
- '/login': Allows users to login by sending a POST request with a JSON object containing their username and password. The endpoint returns a JSON object with a message indicating whether the user is valid or not.
- '/search': Allows users to search for recipes by sending a GET request with a JSON object containing a search query. The endpoint returns a JSON object containing a list of matching recipes.
- '/suggest': Allows users to get recipe suggestions based on a list of keywords by sending a GET request with a JSON object containing the list of keywords. The endpoint returns a JSON object containing a list of suggested recipes.
- '/random': Allows users to get a random recipe by sending a GET request to the endpoint. The endpoint returns a JSON object containing the details of a random recipe.

Attributes:
- app: The Flask application object that provides the RESTful API.
- api: The Flask-Restful API object that handles the routing of requests.

Usage:
- To run the Flask application, call the 'run' method on the app object from the command line: 'python app.py'
- To interact with the API, send HTTP requests to the appropriate endpoint using a tool like Postman or a programming language's built-in HTTP library.
"""


app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(SearchRecipe, '/search')
api.add_resource(SuggestRecipe, '/suggest')
api.add_resource(RandomRecipe, '/random')

if __name__ == '__main__':
    
    app.run(
        debug=True,
        port=5000,
        host='0.0.0.0',
        use_reloader=False
    )
    