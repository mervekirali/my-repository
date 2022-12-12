from flask import Flask, render_template  #Import Flask and render_template modules.

app = Flask(__name__) #Create a flask app

#Create a function named `head` which sends number `number1` and `number2` variables to the `index.html`. 
#Use these variables into the `index.html` file. 
#Assign a URL route the `head` function with decorator `@app.route('/')`.
@app.route('/')
def head():
    return render_template('index.html', number1=10, number2=20)




# Create a function named `number` which sends number `value1` and `value2`
# and sum of them to the `body.html`. Use these variables into the `body.html` file.
# Assign a URL route the `number` function with decorator `@app.route('/sum')`.
@app.route('/sum')
def number():
    x = 15
    y = 20
    return render_template('body.html', value1=x, value2=y, sum=x+y)


if __name__ == '__main__':
    app.run(debug=True)