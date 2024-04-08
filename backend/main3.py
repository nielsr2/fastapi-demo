from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

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

# API endpoint to add a new item
@app.post("/items", response_model=Item)
async def add_item(item: Item):
    data = load_data()
    data.append(item.dict())
    save_data(data)
    return item



