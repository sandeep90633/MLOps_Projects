from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

db = {
    'sandeep': 'pass123',
    'ambati': 'matic123',
    'sunny': 'sunny123'
}

@app.route('/')
def home():
    return render_template("login.html")

@app.route("/login", methods = ['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in db and db[username]==password:
        return redirect(url_for('success', name=username))
    else:
        return redirect(url_for('failure'))

@app.route("/success/<name>")
def success(name):
    return render_template('success.html', username=name)

@app.route("/failure")
def failure():
    return render_template('failure.html')

if __name__ == "__main__":
    app.run(debug=True)