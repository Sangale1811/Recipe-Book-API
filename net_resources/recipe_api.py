import requests
from ai_model_resource.api import SuggestModel

class Recipe():

    """
    Class Recipe()
        A class for retrieving recipes from the MealDB API and generating images for the recipes using the SuggestModel class.

        Attributes:
        -----------
        meal (str): The name of the meal for which to retrieve a recipe.
        endpoint (str): The endpoint URL for the MealDB API.

        Methods:
        --------
        __init__: Initializes the Recipe instance with the appropriate attributes.
        get_recipe: Retrieves a recipe from the MealDB API and generates an image for the recipe using the SuggestModel class.
    """

    def __init__(self, meal_name: str = None) -> None:
        self.meal = meal_name
        self.endpoint = f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal_name}"

    def get_recipe(self, endpoint: str = None) -> tuple:

        result = False
        output = None

        try:
            if endpoint == None:
                response = requests.get(self.endpoint)
            else:
                response = requests.get(endpoint)
        except Exception as err:
            print(f"Some error has occured: {err}")
        if response.status_code == 200 :
            if response.json()["meals"] == None:
                output = {'error': 'No meals found!'}
                return output,result
            
            recipe = response.json()["meals"][0]["strInstructions"]
            ingredients = []
            for i in range(1, 21):
                ingredient = response.json()["meals"][0][f"strIngredient{i}"]
                if ingredient:
                    measure = response.json()["meals"][0][f"strMeasure{i}"]
                    ingredients.append(f"{ingredient}: {measure}")
            
            category = response.json()["meals"][0]["strCategory"]
            area = response.json()["meals"][0]["strArea"]
            tags = response.json()["meals"][0]["strTags"]
            if tags:
                tags = tags.split(",")
                keywords = [category, area] + tags
            else:
                keywords = [category, area]
            
            output = {
                'meal_name': str(response.json()["meals"][0]["strMeal"]),
                'meal_image_b64': SuggestModel().generate_image(str(response.json()["meals"][0]["strMeal"])),
                'recipe': recipe,
                'ingredients': ingredients,
                'keywords': keywords
            }
        else :
            output = {'error': f'Internal Server Error. Hint : Api returned {response.status_code} response.'}

        return output,result
