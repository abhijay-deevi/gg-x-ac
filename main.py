#importing things
from flask import Flask, redirect, url_for, render_template, request
import data

app = Flask(__name__)

# Starting the app routes
# This is the stuff that lets the website redirect to different pages

# This is the first page that comes up when you start the program
@app.route("/landing")
@app.route("/")
def landing():
    return render_template("landing.html")

# This is the home page where you see trending projects and things like that
@app.route("/home")
def home():
    return render_template("apcoxgg.html")

# This is the slackbots page where it gives the embedded files to each person
@app.route("/slackbots")
def slackbots():
    return render_template("about.html", groupdatalist=data.groupdata())

# This is the route to the Kevin page which holds all his embedded files
@app.route("/kevin")
def kevin():
    return render_template("indivabout.html", data=data.kevin())

# This is the route to the Abhijay page which holds all his embedded files
@app.route("/abhijay")
def abhijay():
    return render_template("indivabout.html", data=data.abhijay())

# This is the route to the Paul page which holds all his embedded files
@app.route("/paul")
def paul():
    return render_template("indivabout.html", data=data.paul())

# This is the route to the Travis page which holds all his embedded files
@app.route("/travis")
def travis():
    return render_template("indivabout.html", data=data.travis())

# This is the route to the Gavin page which holds all his embedded files
@app.route("/gavin")
def gavin():
    return render_template("indivabout.html", data=data.gavin())

# This is the route to the base product view page where you can just see the basic product designs
@app.route("/baseview")
def baseview():
    return render_template("base-productview.html")

# This is the route to the shoe models
@app.route("/shoebaseview")
def shoebaseview():
    return render_template("base-productview-shoe.html")

# This is the route to the apco pink liquid looking shirt product page
@app.route("/APCOFluid")
def APCOFluid():
    return render_template("apco-fluid.html")

# This is the route to the apco adidas pink shoes product page
@app.route("/APCOSuperstar")
def APCOSuperstar():
    return render_template("apco-superstar.html")

# This is the route to the godly goat firework shirt product page
@app.route("/GGFireworks")
def GGFireworks():
    return render_template("gg-fireworks.html")

# This is the route to the godly goat adidas shoes product page
@app.route("/GGSuperstar")
def GGSuperstar():
    return render_template("gg-superstar.html")

# This is the route to the products page where it will show you all the products we currently have
@app.route("/products")
def products():
    return render_template("products.html")

# This is the route to the the cart where you can pay for the merch and see what you are going to buy
@app.route("/cart")
def cart():
    return render_template("cart.html")

# This is the stuff that gets the POST methods
# It allows the user to input user information --> In this case it's their card information
# It also saves their information in variables so they can see the purchase screen
@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method=='POST':
        form = request.form
        firstname = (form['firstname'])
        lastname = (form['lastname'])
        address = (form['address'])
        extra_address = (form['extra_address'])
        city = (form['city'])
        state = (form['state'])
        zipcode = (form['zipcode'])
        phonenumber = (form['phonenumber'])
        cardnumber = (form['cardnumber'])
        protectedcardnumber = cardnumber[-4] + cardnumber[-3] + cardnumber[-2] + cardnumber[-1]
        expiration = (form['expiration'])
        cvc = (form['cvc'])
        info = {"firstname": firstname, "lastname": lastname, "address": address, "extra_address": extra_address, "city": city, "state": state, "zipcode": zipcode,
                "phonenumber": phonenumber,
                "protectedcardnumber": protectedcardnumber, "expiration": expiration, "cvc": cvc}
    return render_template("success.html", data=info)


if __name__ == "__main__":
    app.run(debug=True)
