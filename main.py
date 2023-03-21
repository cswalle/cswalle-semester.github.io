from flask import Flask, render_template,request
import json


with open('config.json','r') as c:
    params=json.load(c)["params"]

# create flask app
app = Flask(__name__)


@app.route('/')
def home(method=['GET','POST']):
    return render_template('semester.html')


@app.route("/<string:iter_slug>")
def semester(iter_slug):
    if iter_slug == "second-slug":
        return render_template('/semester/secondsem.html')
    if iter_slug == "fourth-slug":
        return render_template('/semester/fourthsem.html')
    if iter_slug == "sixth-slug":
        return render_template('/semester/sixthsem.html')
    if iter_slug == "first-slug":
        return render_template('/semester/defaultsem.html',post="First")
    if iter_slug == "third-slug":
        return render_template('/semester/defaultsem.html',post="Third")
    if iter_slug == "fifth-slug":
        return render_template('/semester/defaultsem.html',post="Fifth")
    if iter_slug == "seventh-slug":
        return render_template('/semester/defaultsem.html',post="Seventh")
    if iter_slug == "eigth-slug":
        return render_template('/semester/defaultsem.html',post="Eigth")

    return render_template('semester.html',params=params)

app.run(host="0.0.0.0",port=5000,debug=True)