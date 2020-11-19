import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

pictures = [{
        "Id": 1,
        "Poster": "http://www.livingstonmanor.net/HoosBuilding/TN_LMtoday-HoodBuilding.JPG",
        "Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eu dapibus risus. Sed imperdiet nibh nunc. Quisque non tempus nisi. Donec sed massa pretium, finibus purus ac, rhoncus est. Donec et libero urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas massa nisl, vulputate non dui eu, hendrerit pharetra elit.",
        "Location": "Stony Brook"
    },
    {
        "Id": 2,
        "Poster": "http://www.livingstonmanor.net/LM-FloodOf2010/LM-Flood2010-Sunoco.jpg",
        "Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eu dapibus risus. Sed imperdiet nibh nunc. Quisque non tempus nisi. Donec sed massa pretium, finibus purus ac, rhoncus est. Donec et libero urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas massa nisl, vulputate non dui eu, hendrerit pharetra elit.",
        "Location": "Stony Brook"
    },
    {
        "Id": 3,
        "Poster": "http://www.livingstonmanor.net/RussellHouse/LM-RussellHouse2009.JPG",
        "Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eu dapibus risus. Sed imperdiet nibh nunc. Quisque non tempus nisi. Donec sed massa pretium, finibus purus ac, rhoncus est. Donec et libero urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas massa nisl, vulputate non dui eu, hendrerit pharetra elit.",
        "Location": "Stony Brook"
    },
    {
        "Id": 4,
        "Poster": "http://livingstonmanor.net/FredPIX2/IMG_0789%20-%20Copy.JPG",
        "Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eu dapibus risus. Sed imperdiet nibh nunc. Quisque non tempus nisi. Donec sed massa pretium, finibus purus ac, rhoncus est. Donec et libero urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas massa nisl, vulputate non dui eu, hendrerit pharetra elit.",
        "Location": "Stony Brook"
    },
    {
        "Id": 5,
        "Poster": "https://images.squarespace-cdn.com/content/v1/534d8565e4b0c7f5e4fcb4f7/1562030061043-ICZGG34BMCXHR40HHXGX/ke17ZwdGBToddI8pDm48kFyD7pzB8zoMIVY5aiUuFlp7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0jG2lbcDYBOeMi4OFSYem8DMb5PTLoEDdB05UqhYu-xbnSznFxIRsaAU-3g5IaylIg/foster-supply-hospitality-ARNOLD-2019-06-Conservatory-Food-Scott-Yoga-Exteriors-Lawrence-Braun-0001-LB2_2700.jpg",
        "Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eu dapibus risus. Sed imperdiet nibh nunc. Quisque non tempus nisi. Donec sed massa pretium, finibus purus ac, rhoncus est. Donec et libero urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas massa nisl, vulputate non dui eu, hendrerit pharetra elit.",
        "Location": "Stony Brook"
    },
]

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def main():
	return render_template('main.html', pictures=pictures)

@app.route('/upload')
def upload_form():
	return render_template('upload.html')

@app.route('/uploaded', methods=['GET', 'POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		return render_template('upload.html', filename=filename)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run()