# # Python3 program for above approach
# from flask import Flask, render_template
# appapp = Flask(__name__)
# def head():    
#      return render_template('index.html', message='This is my first conditions experience')




# Import Flask modulesfrom flask import Flask, render_template
# Create an object named appapp = Flask(__name__)
# Create a function named head which shows the massage as "This is my first conditions experience" in `index.html`# and assign to the route of ('/')

# Create a function named header which prints numbers elements of list one by one in `body.html`# and assign to the route of ('/mylist')@app.route('/mylist')def header():    mynames = ['Altaz', 'Xi', 'Pratibah']    return render_template('body.html', object=mynames)
# run this app in debug mode on your local.if __name__ == '__main__':    app.run(debug=True)





# Function to calculate Roman values
def intToRoman(num):
  
    # Storing roman values of digits from 0-9
    # when placed at different places
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
  
    # Converting to roman
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
  
    ans = (thousands + hundreds +
           tens + ones)
  
    return ans
  
# Driver code
if __name__ == "__main__":
    number = int(input("Please enter a number: "))
    print(intToRoman(number))

