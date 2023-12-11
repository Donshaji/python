from flask import Flask,render_template
app = Flask(__name__)
posts=[
    {
        'auther':'corey schafer',
        'title':'Blog post 1',
        'date_posted':'April 20,2018',
    },
    {
        'auther':'Jane Doe',
        'title':'Blog post 2',
        'date_posted':'April 25,2018',
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)
@app.route("/about")
def about():
    return render_template('about.html')
if __name__=='__main__':
    app.run(debug=True)