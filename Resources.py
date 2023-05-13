from ai_model_resource.api import SuggestModel
#
from dsbda_module import SimilarRecipe
#
from net_resources.cloud_db import StoreOnCloud
from net_resources.recipe_api import Recipe
#
from flask_restful import Resource, reqparse, request


class UserRegister(Resource):
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('firstName', type=str, required=True, help='First Name is required')
        self.parser.add_argument('lastName', type=str, required=True, help='Last Name is required')
        self.parser.add_argument('username', type=str, required=True, help='Username is required')
        self.parser.add_argument('email', type=str, required=True, help='Email is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')   

    def post(self):
        data = self.parser.parse_args()
        output, result = StoreOnCloud().insert_user(username=data['username'], password=data['password'], email=data['email'],firstName=data['firstName'],lastName=data['lastName'])
        return output



class UserLogin(Resource):
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, required=True, help='Email is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')

    def post(self):
        data = self.parser.parse_args()
        output, result = StoreOnCloud().retrieve_user(email=data['email'], password=data['password'])
        return output


class SearchRecipe(Resource):
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('meal', type=str, required=True, help='Meal is required')

    def post(self):
        data = self.parser.parse_args()
        output, result = Recipe(data['meal']).get_recipe()
        return output

class SuggestRecipe(Resource):
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('keywords', type=str, required=True, help='Keywords are required')  

    def post(self):
        data = self.parser.parse_args()
        keywords = data['keywords'].split()
        output, result = SimilarRecipe().getSimilarRecipes(keywords)
        return output


class RandomRecipe(Resource):
    def __init__(self) -> None:
        pass

    def get(self):
        random_endpoint = "https://www.themealdb.com/api/json/v1/1/random.php"
        output, result = Recipe().get_recipe(random_endpoint)
        return output
