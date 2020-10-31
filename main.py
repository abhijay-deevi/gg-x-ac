from flask import Flask, redirect, url_for, render_template

app= Flask(__name__)

@app.route("/landing")
@app.route("/")
def landing():
	return render_template("landing.html")

@app.route("/home")
def home():
	return render_template("apcoxgg.html")

@app.route("/baseview")
def baseview():
	return render_template("base-productview.html")

@app.route("/shoebaseview")
def shoebaseview():
	return render_template("base-productview-shoe.html")

@app.route("/APCOFluid")
def APCOFluid():
	return render_template("apco-fluid.html")

@app.route("/APCOSuperstar")
def APCOSuperstar():
	return render_template("apco-superstar.html")

@app.route("/GGFireworks")
def GGFireworks():
	return render_template("gg-fireworks.html")

@app.route("/GGSuperstar")
def GGSuperstar():
	return render_template("gg-superstar.html")

if __name__ == "__main__":
	app.run(debug=True)