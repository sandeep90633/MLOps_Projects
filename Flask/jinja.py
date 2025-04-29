# Building URL Dynamically
# Variable Rule
# Jinja 2 Template Engine

# Jinja 2 Tempalte Engine
'''
{{ }} expressions to print output in html
{%....%} conditions, for loops or if
{#....#} this is for comments
'''
from flask import Flask, render_template, request, url_for, redirect

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the first flask run."
 
@app.route("/submit", methods=['POST','GET'])
def submit():
    result = 0
    if request.method=='POST':
        num1 = float(request.form['input1'])
        num2 = float(request.form['input2'])
        operator = request.form['operator']

        # Perform the calculation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = None
                
        return redirect(url_for("result", score= result))
    
    return render_template('form.html')

@app.route("/result/<int:score>")
def result(score):
    status = ""
    if score>=50:
        status = "PASSED"
    else:
        status = "FAILED"
    
    return render_template('result.html', status=status, score=score) 

if __name__ == "__main__":
    app.run(debug = True)