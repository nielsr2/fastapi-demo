# instead of using react, this file uses Jinja2 to render the HTML page  - Jinja2 is a templating engine for Python, which allows you to embed Python code in HTML files.
# see /templates/index.html for the HTML file that is rendered



from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Load data from the JSON file
def load_data():
    with open("../data.json", "r") as file:
        data = json.load(file)
    return data

# Serve the index page with items
@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    items = load_data()
    return templates.TemplateResponse("index.html", {"request": request, "items": items})
