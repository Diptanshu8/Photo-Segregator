from flask import Flask, render_template, request, url_for, redirect
import os
from flask_images import Images


app = Flask(__name__)
app.secret_key = "temp"
#images = Images(app)

def get_images_from_static():
	images = [item for item in os.listdir("static") if ".jpg" in item]
	return images

@app.route('/')
def home_page():
	images=get_images_from_static()
	return render_template("base.html",images= images)

@app.route('/scan_image', methods=['POST','GET'])
def scan_image():
	print("Inside scan_image")
	print(request)
	print(request.data.decode())
	# Get image name from the result by searching for .jpg ext as of now. Extend to other extensions too.
	# Process image and add the processed image with squares to the image list and render
	images=get_images_from_static()
	return render_template("base.html",images= images)

app.run(host="0.0.0.0", debug=True)
