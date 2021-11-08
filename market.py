from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homePage():
    return render_template("home.html")

@app.route('/market')
def marketPage():
	return render_template("market.html")









