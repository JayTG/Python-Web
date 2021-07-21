from flask import Flask
app = Flask(__name__)
#Home
@app.route("/")
def home():
    return "<h1>Home Page</h1>"
#About
@app.route("/about")
def about():
    return "<h1>About</h1>"


if __name__ == '__main__':
    app.run(debug=True)