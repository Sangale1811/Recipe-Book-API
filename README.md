# **Recipe Book API**
This API provides several endpoints to manage user registration and profile, search for recipes, and suggest random recipes.

## **Endpoints**
### **User Registration and Profile**
**Endpoint: /register**

**Method: POST**

**Description:** This endpoint allows users to register an account and create a profile.

**Request Parameters:**

- **username** (required): The username of the user.
- **email** (required): The email address of the user.
- **password** (required): The password for the user's account.
- **first_name** (optional): The first name of the user.
- **last_name** (optional): The last name of the user.

**Response:**

- **message**: A success or error message.
- **user**: The user's profile information.

### **Search Recipe**
**Endpoint: /search**

**Method: GET**

**Description:** This endpoint searches for recipes based on the search query and returns the results in JSON format. It uses FreeMealDB API to fetch the recipe details.

**Request Parameters:**

- **query** (required): The search query for the recipe.

**Response:**

- **meals**: A list of recipes matching the search query, where each recipe contains:
- **strMeal**: The name of the meal.
- **strInstructions**: The recipe instructions.
- **strIngredient1** - strIngredient20: The list of ingredients.
- **strMealThumb**: The URL of the image.

### **Suggest Recipes**
**Endpoint: /suggest**

**Method: GET**

**Description:** This endpoint suggests 3-5 recipes based on the search query and returns the results in JSON format.

**Request Parameters:**

- **query** (required): The search query for the recipe.

**Response:**

- meals: A list of 3-5 recipes suggested based on the search query, where each recipe contains:
    - strMeal: The name of the meal.
    - strInstructions: The recipe instructions.
    - strIngredient1 - strIngredient20: The list of ingredients.
    - strMealThumb: The URL of the image.

### **Random Recipes**
**Endpoint: /random**

**Method: GET**

**Description:** This endpoint returns 5 random recipes in JSON format.

**Request Parameters:**

None

**Response:**

- **meals**: A list of 5 random recipes, where each recipe contains:
    - **strMeal**: The name of the meal.
    - **strInstructions**: The recipe instructions.
    - **strIngredient1** - strIngredient20: The list of ingredients.
    -  **strMealThumb**: The URL of the image.

### Database
This API uses MongoDB to store user registration and profile information. Cloud-based MongoDB is used to perform database operations.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the libraries required for the api.

```bash
pip install -r 'path/to/requirements.txt'
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.