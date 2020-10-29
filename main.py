from flask import Flask, redirect, url_for, render_template

app= Flask(__name__)

@app.route("/landing")
@app.route("/")
def landing():
	return render_template("landing.html")

@app.route("/home")
def home():
	return render_template("acxgg.html")

@app.route("/baseview")
def baseview():
	return render_template("base-productview.html")

@app.route("/ACMain")
def ACMain():
	return render_template("AC-Main.html")

@app.route("/ACHoodie")
def ACHoodie():
	return render_template("ac-hoodie.html")

if __name__ == "__main__":
	app.run(debug=True)