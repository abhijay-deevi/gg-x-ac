from flask import Flask, redirect, url_for, render_template

app= Flask(__name__)

@app.route("/landing")
@app.route("/")
def landing():
	return render_template("landing.html")

@app.route("/home")
def home():
	return render_template("acxgg.html")

@app.route("/item")
def item():
	return render_template("itempagetemp.html")

if __name__ == "__main__":
	app.run(debug=True)