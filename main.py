from flask import Flask, redirect, url_for, render_template
import data

app= Flask(__name__)

@app.route("/landing")
@app.route("/")
def landing():
	return render_template("landing.html")

@app.route("/home")
def home():
	return render_template("apcoxgg.html")

@app.route("/slackbots")
def slackbots():
	return render_template("about.html", groupdatalist=data.groupdata())

@app.route("/kevin")
def kevin():
	return render_template("indivabout.html", data=data.kevin())

@app.route("/abhijay")
def abhijay():
	return render_template("indivabout.html", data=data.abhijay())

@app.route("/paul")
def paul():
	return render_template("indivabout.html", data=data.paul())

@app.route("/travis")
def travis():
	return render_template("indivabout.html", data=data.travis())

@app.route("/gavin")
def gavin():
	return render_template("indivabout.html", data=data.gavin())

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