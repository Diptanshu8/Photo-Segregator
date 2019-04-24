from flask import Flask, render_template, request, url_for
import os


app = Flask(__name__)
@app.route('/')
def index():
    return render_template("base.html")
app.run(host="0.0.0.0")
