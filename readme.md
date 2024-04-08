This repo showcases a FastAPI & React web application that loads data from a json file, and displays them with react components.

To get this project up and running we need to

1. Creating a virtual environment (in order to isolate the dependencies(libraries, etc))

2. install the python dependencies from the requirements.txt file
   - pip install -r requirements.txt

You can generate a requirements.txt file by running the following command:
pip freeze > requirements.txt

3. install the nodejs dependencies

   - npm install

4. Run the FastAPI server

   1. cd into 'backend' directory
   2. uvicorn main:app --reload

5. Run the React app
   1. cd into 'frontend' directory
   2. npm start

---

Main.py - Is the simplest fastAPI example - it loads some 'items' from data.json and returns them as a response (to react)
main2.py - Is the fastAPI example, not with react, but just using jinja templates
main3.py - Is the fastAPI example - with ability to add new 'items' to the list of items (json file)
main4.py - uses huggingface api for silly check of whether image is of dog - only images of dogs can be added to the database

(note that there's 3 versions of app.js that correspond to the different main.py files)

Exercise ideas:

- Add a new page that displays the details of a single item
- implement CRUD operations (Create, Read, Update, Delete) for the items
- Enhance the UI/UX - explore React libraries like Material-UI, Ant Design, etc. or other components
  - see https://github.com/brillout/awesome-react-components

That's when the fun begins!  🚀