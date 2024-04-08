from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json 

app = FastAPI()

# Add CORS middleware to allow requests from the frontend
# CORS (Cross-Origin Resource Sharing) is a security feature implemented in web browsers to allow requests from one domain to another domain. 

# Because the frontend and backend are running on different ports, the browser blocks the requests by default. 

#  Usually, you would want to restrict the origins to only the frontend domain, but for development purposes, we can allow all origins by setting allow_origins=["*"].

# put simply: you wouldn't want facebook to load a .js file from www.supersketchywebsite.com and then have that .js file send a request to facebook.com to get your personal data.

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
    with open("../data.json", "r") as file: # if path was just "data.json", it would look for the file in the same directory as the script (main.py) - adding the ".." moves up one directory
        data = json.load(file)
    return data

# API endpoint to get the list of items
@app.get("/items", response_model=List[Item])
async def read_items():
    return load_data()


# API endpoint to get a specific item
# @app.get("/items/{item_id}")
# async def read_item(item_id):
    # return {"item_id": item_id}

