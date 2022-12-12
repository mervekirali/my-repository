from flask import Flask

app = Flask(__name__) #Create a flask web app


#A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.

@app.route('/')       #Assign a URL route the hello function with decorator @app.route('/')
def hello():          #Create a function called hello and return hello world string

    return "Hello World"

@app.route('/second')
def second():

    return "This is the second page"

@app.route('/third/subthird')
def third():

    return "This is the subpage of the third page"


@app.route('/forth/<string:id>')   #Create a dynamic URL which takes id number dynamically and return with a message which show id of page.
def fourth(id):

    return f"The id of this page is {id}"

if __name__ == '__main__': #the main file is hello-world-app.py, so this is the main file to be run
    app.run(debug=True)

