# Import flask module
from flask import Flask

# Create an object named `app` from imported Flask module.
app = Flask(__name__)

# Function `hello` which returns a string `Hello World`.
# Assign a URL route the `hello` function with decorator `@app.route('/')`.
@app.route('/')
def hello():
    return "<h1>Hello World</h1>"

# Function `second` which returns a string `This is the second page` 
# Assign a URL route the `second` function with decorator `@app.route('/second')`. 
@app.route('/second')
def second():
    return "<h2>This is the second page</h2>"

# Function `third` which returns a string `This is the subpage of third page` 
# Assign a URL route the `third` function with decorator `@app.route('/third/subthird')`. 
@app.route('/third/subthird')
def third():
    return "<h2>This is the subpage of the third page</h2>"

# Dynamic url which takes id number dynamically 
# Function 'fourth' which returns a massage which show id of page.
@app.route('/fourth/<string:id>')
def fourth(id):
    return f'This is a page id {id}'

if __name__ == '__main__':
    app.run(debug=False)
