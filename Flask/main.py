from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the first flask run."

@app.route("/services")
def features():
    return render_template('services.html')

@app.route("/info")
def info():
    return render_template("info.html")

if __name__ == "__main__":
    app.run(debug = True)