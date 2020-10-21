from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    #function use Flask import (Jinga) to render an HTML template
    return render_template("acxgg.html")

@app.route('/godlygoats')
def kevin():
    return render_template("godlygoats.html")

@app.route('/albertpani')
def abhijay():
    return render_template("albertpani.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='0.0.0.0')