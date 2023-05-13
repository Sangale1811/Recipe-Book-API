import base64
import requests


class SuggestModel:

    """
    Class SuggestModel()
        A class that generates an image based on the given dialogue using an API from Hugging Face.

        Attributes:
        -----------
        endpoint (str): The URL endpoint for the API.
        headers (dict): A dictionary containing the authorization header.

        Methods:
        --------
        __init__(self) -> None:
            Initializes the `SuggestModel` object with an endpoint URL and headers for authorization.

        __image_to_base64(self, image):
            Converts an image to base64 format.

        generate_image(self, dialogue):
            Generates an image based on the given dialogue using the API. If an error occurs while generating an image, it returns a default image from the `https://picsum.photos/200` endpoint.
    """

    def __init__(self) -> None:
        self.endpoint = "https://api-inference.huggingface.co/models/prompthero/openjourney-v4"
        self.headers = {"Authorization": "Bearer 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"}  # Need Token from Hugging face

    def __image_to_base64(self, image):
        base64_image = None
        try:
            base64_image = base64.b64encode(image)
            base64_image = 'data:image/jpeg;base64,' + base64_image.decode('utf-8')
        except Exception as err:
            print("An exception has occured")
        
        return base64_image

    def generate_image(self,dialogue):
        image = None
        payload = {
	    "inputs": str(dialogue),
        }
        try:
            response = requests.post(self.endpoint, headers=self.headers, json=payload)
            image_bytes = response.content
        except Exception as err:
            print("An error occured while generating an image")

        b64_image = None

        if image_bytes:
            b64_image = self.__image_to_base64(image_bytes)
        else:
            image_bytes = requests.get("https://picsum.photos/200")
            b64_image = self.__image_to_base64(image_bytes)

        return b64_image

