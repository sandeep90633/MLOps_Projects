from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the first flask run."

@app.route("/features")
def features():
    return "Not yet developed. Still need to work."

if __name__ == "__main__":
    app.run(debug = True)