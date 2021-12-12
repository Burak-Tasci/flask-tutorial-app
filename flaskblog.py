from flask import Flask, render_template
app = Flask(__name__)

posts = [

	{
		'author': 'Corey Schafer',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted':'April 20, 2018'
	},
	{
		'author': 'John Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted':'April 25, 2018'
	}
]


@app.route("/")
@app.route("/home")
def HomePage():
	return render_template("home.html", posts=posts)

@app.route("/about")
def AboutPage():
	return render_template("about.html", title="About")
