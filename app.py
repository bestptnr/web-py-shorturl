
import pyshorteners
from flask import Flask, render_template,request,url_for

import requests



app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        
        return render_template("index.html",data="")
    if request.method == "POST":
        url = request.form['url']
        long_url = url
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(long_url)
        return render_template("index.html",data=short_url)

if __name__ == "__main__":
    app.run(debug=True)