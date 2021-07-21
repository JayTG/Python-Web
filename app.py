from flask import Flask, render_template
app = Flask(__name__)

#blog post content list
posts = [
    {
        'author' : 'Dan',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 20 2020'
    },
    {
        'author' : 'Dave',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'April 21 2020'
    } 
]

#Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

#About page
@app.route("/about")
def about():
    return render_template('about.html')

# if run on python go to debug mode
if __name__ == '__main__':
    app.run(debug=True)