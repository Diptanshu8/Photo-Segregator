from flask import Flask, render_template, request, url_for
import os
from flask_images import Images


app = Flask(__name__)
app.secret_key = "temp"
images = Images(app)

def get_images_from_static():
	return os.listdir("static")
@app.route('/')
def index():
	images=get_images_from_static()
	return render_template("base.html",images= images)
app.run(host="0.0.0.0")
