
import os
import uvicorn
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

from .gemini_client import GeminiClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="webapp/static"), name="static")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows the React app to communicate with the backend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

gemini_client = GeminiClient()

@app.post("/generate_image/")
async def generate_image(prompt: str = Form(...), image: UploadFile = File(...)):
    print("Received request to generate image.")
    image_bytes = await image.read()
    pil_image = Image.open(io.BytesIO(image_bytes))

    print("Sending request to Gemini API...")
    texts, images = gemini_client.respond([prompt, pil_image])
    print("Received response from Gemini API.")

    if images:
        # Save the generated image to a file
        output_image_path = "webapp/static/latest_generated_image.png"
        with open(output_image_path, "wb") as f:
            f.write(images[0])
        print(f"Saved generated image to {output_image_path}")

        print("Sending image back to frontend.")
        return Response(content=images[0], media_type="image/png")
    else:
        print("Error: Image could not be generated.")
        return {"error": "Image could not be generated"}, 400

if __name__ == "__main__":
    print("To run the server with reload, use the following command:")
    print("uvicorn webapp.backend.server:app --host 0.0.0.0 --port 8000 --reload")
    print("\nStarting server with uvicorn.run() for basic execution...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
