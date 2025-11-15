from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("You've visited the Hello page")
    return "Hello, World!"

@app.route('/about')
def about():
    print("Now this is the ABOUT page, you've visited")
    return "About page"