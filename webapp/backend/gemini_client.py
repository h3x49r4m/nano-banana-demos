#!/usr/bin/env python
import os
import uuid
from io import BytesIO

from PIL import Image
from google import genai

GEMINI_API_KEY =  open(os.path.join(os.path.dirname(__file__), '..', '..', '.configs', 'gemini.txt'), 'r').read().strip()

class GeminiClient:

    def __init__(self, api_key=GEMINI_API_KEY, model="gemini-2.5-flash-image-preview"):
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def respond(self, contents, is_verbose=True):
        """
        Arguments:
        - text to image: contents=[prompt]
        - edit image: contents=[prompt, Image.open(image_path)]
        - combine images: contents=[Image.open(image1), Image.open(image2), prompt]
        """
        response = self.client.models.generate_content(model=self.model, contents=contents)
        texts, images = self._response_stream(response)
        return texts, images


    def _response_stream(self, response, is_verbose=True):
        texts = []
        images = []

        for part in response.candidates[0].content.parts:
            if part.text is not None:
                texts.append(part.text)
                if is_verbose:
                    print(part.text)

            elif part.inline_data is not None:
                images.append(part.inline_data.data)
                if is_verbose:
                    image = Image.open(BytesIO(part.inline_data.data))
                    image_path = f"{os.path.join(os.path.dirname(__file__), '_out', 'image_{uuid.uuid4()}.png')}"
                    image.save(image_path)
                    print(f"INFO: image saved at {image_path}")

        return texts, images

if __name__ == '__main__':
    client = GeminiClient()
    texts, images = client.respond(["hello world"])
    print(texts)
