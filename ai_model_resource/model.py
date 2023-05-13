from diffusers import StableDiffusionPipeline
import torch
import base64
import requests
import os


class SuggestModel:

    """
    Class SuggestModel()
        A class that generates an image based on the given dialogue using a pretrained model "Stable Diffusion" from Hugging Face.

        Attributes:
        -----------
        model_id (str): Model name for the model used.
        model (PipeLine): Model Pipeline used to generate images.

        Methods:
        --------
        __init__(self) -> None:
            Initializes the `SuggestModel` object with an endpoint URL and headers for authorization.

        __image_to_base64(self, image):
            Converts an image to base64 format.

        generate_image(self, dialogue):
            Generates an image based on the given dialogue using the pretrained model. If an error occurs while generating an image, it returns a default image from the `https://picsum.photos/200` endpoint.
    """

    def __init__(self) -> None:
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        self.model_id = "runwayml/stable-diffusion-v1-5"
        self.model = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16)

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
        try:
            image = self.model(dialogue).images[0]
        except Exception as err:
            print("An error occured while generating an image")

        b64_image = None

        if image:
            b64_image = self.__image_to_base64(image)
        else:
            image = requests.get("https://picsum.photos/200")
            b64_image = self.__image_to_base64(image)

        return b64_image

