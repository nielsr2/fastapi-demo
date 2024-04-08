
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List
import httpx
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# Define the model for items
class Item(BaseModel):
    name: str
    description: str
    imageUrl: str

# Load data from the JSON file
def load_data():
    with open("../data.json", "r") as file:
        data = json.load(file)
    return data

# Save data to the JSON file
def save_data(data):
    with open("../data.json", "w") as file:
        json.dump(data, file, indent=4)

# API endpoint to get the list of items
@app.get("/items", response_model=List[Item])
async def read_items():
    return load_data()


@app.post("/items", response_model=Item)
async def add_item(item: Item):
    encoded_image = await fetch_and_encode_image(item.imageUrl)
    classification_result = await classify_image_async(encoded_image, "openai/clip-vit-large-patch14", hf_api_token)
    print(classification_result)
    # results look like [{'score': 0.9617117047309875, 'label': 'dog'}, {'score': 0.030612345784902573, 'label': 'bear'}, {'score': 0.006349625065922737, 'label': 'bacon'}, {'score': 0.0013263566652312875, 'label': 'cat'}]
    if classification_result[0]["label"] != "dog":
        print("Dog not detected!")
        raise HTTPException(status_code=400, detail="Only dogs are allowed!")
    else:
        print("Dog detected!")
        data = load_data()
        data.append(item.dict())
        save_data(data)
        return item



# Fetches an image from a URL and encodes it in base64 (string! )
async def fetch_and_encode_image(image_url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(image_url)
        response.raise_for_status()  # Ensure the request was successful
        image_bytes = response.content
    
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")
    return encoded_image


# send the image to the model for classification
async def classify_image_async(encoded_image: str, model: str, hf_api_token: str) -> dict:
    payload = {
        "parameters": {"candidate_labels": ['dog', 'cat', 'bacon', 'bear']},
        "inputs": encoded_image
    }
    headers = {"Authorization": f"Bearer {hf_api_token}"}
    API_URL = f"https://api-inference.huggingface.co/models/{model}"

    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, headers=headers, json=payload, timeout=60.0)
        response.raise_for_status()  # Ensure the request was successful

    return response.json()

hf_api_token = "get your token from huggingface.co"