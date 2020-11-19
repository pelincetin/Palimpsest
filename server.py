import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

pictures = [{
        "Id": 1,
        "Picture": "https://wmho.org/wp-content/uploads/2017/04/IMG_0464.jpg",
        "Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eu dapibus risus. Sed imperdiet nibh nunc. Quisque non tempus nisi. Donec sed massa pretium, finibus purus ac, rhoncus est. Donec et libero urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas massa nisl, vulputate non dui eu, hendrerit pharetra elit.",
        "Location": "Stony Brook"
    },
    {
        "Id": 2,
        "Poster": "https://communityimpact.com/uploads/images/2020/04/09/50369.JPG",
        "Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eu dapibus risus. Sed imperdiet nibh nunc. Quisque non tempus nisi. Donec sed massa pretium, finibus purus ac, rhoncus est. Donec et libero urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas massa nisl, vulputate non dui eu, hendrerit pharetra elit.",
        "Location": "Stony Brook"
    },
    {
        "Id": 3,
        "Poster": "https://m.media-amazon.com/images/M/MV5BY2QzYTQyYzItMzAwYi00YjZlLThjNTUtNzMyMDdkYzJiNWM4XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
        "Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eu dapibus risus. Sed imperdiet nibh nunc. Quisque non tempus nisi. Donec sed massa pretium, finibus purus ac, rhoncus est. Donec et libero urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas massa nisl, vulputate non dui eu, hendrerit pharetra elit.",
        "Location": "Stony Brook"
    },
    {
        "Id": 4,
        "Poster": "https://m.media-amazon.com/images/M/MV5BY2QzYTQyYzItMzAwYi00YjZlLThjNTUtNzMyMDdkYzJiNWM4XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
        "Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eu dapibus risus. Sed imperdiet nibh nunc. Quisque non tempus nisi. Donec sed massa pretium, finibus purus ac, rhoncus est. Donec et libero urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas massa nisl, vulputate non dui eu, hendrerit pharetra elit.",
        "Location": "Stony Brook"
    },
    {
        "Id": 5,
        "Poster": "https://m.media-amazon.com/images/M/MV5BY2QzYTQyYzItMzAwYi00YjZlLThjNTUtNzMyMDdkYzJiNWM4XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
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