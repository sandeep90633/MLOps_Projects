from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the first flask run."

@app.route("/services", methods=['GET'])
def features():
    return render_template('services.html')

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/form", methods=['GET','POST'])
def form():
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
                result = "Error: Division by zero"
        else:
            result = "Invalid operator"
        return f"Result is {result}"
    return render_template('form.html')

@app.route("/submit", methods=['GET','POST'])
def submit():
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
                result = "Error: Division by zero"
        else:
            result = "Invalid operator"
        return f"Result is {result}"
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug = True)