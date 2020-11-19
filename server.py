import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

current_id = 6
pictures = [{
		"Id": 1,
		"Poster": "http://www.livingstonmanor.net/HoosBuilding/TN_LMtoday-HoodBuilding.JPG",
		"Description": "Over the course of the past number of years, flooding along the river and creeks that flow through Livingston Manor has inflicted serious property damage upon the many residences unfortunate enough to be in the path of the river valley's designated flood-plane. Still, the devastation caused over the course of the past few years by these floodwaters pales in comparison to the destruction amassed in just a few short hours by the work of large machines designed to destroy.",
		"Location": "Livingston Manor"
	},
	{
		"Id": 2,
		"Poster": "http://www.livingstonmanor.net/LM-FloodOf2010/LM-Flood2010-Sunoco.jpg",
		"Description": "Heavy rainfall during the evening of September 30th and the early morning hours of October 1st, estimated by some to total six inches of rain, drenched Livingston Manor and its surroundings, quickly filling the previously water-starved local streams and creeks with floodwaters. Considering the experiences from the recent flooding events at the Manor, this episode would probably be considered minor; unless, of course you are one of the residents still remaining in the flood prone areas.",
		"Location": "Livingston Manor"
	},
	{
		"Id": 3,
		"Poster": "http://www.livingstonmanor.net/RussellHouse/LM-RussellHouse2009.JPG",
		"Description": "Livingston Manor has long had a flare for the dramatic, the usual episodes being water related. Yesterday afternoon, however, added a new chapter in Manor misery; fire. In what sounded like the repeated percussion of cannons, the propane tanks alongside the Hoos building exploded, sending shock waves that broke windows and could be felt throughout the downtown section of the village as far away as Peck's Market.",
		"Location": "Livingston Manor"
	},
	{
		"Id": 4,
		"Poster": "http://livingstonmanor.net/FredPIX2/IMG_0789%20-%20Copy.JPG",
		"Description": "While working on dismantling the approaches to the Beaverkill Covered Bridge during the winter of 2016-17, the bridge restoration work crew unearthed a cache of hides buried within the earthen ramp leading to the bridge’s eastern portal. These hides assumedly date back to the nineteenth century tannery of Wm. Ellswoth & Co. that was located at what is now the Beaverkill Campsite, next to the bridge.",
		"Location": "Beaverkill Covered Bridge"
	},
	{
		"Id": 5,
		"Poster": "https://images.squarespace-cdn.com/content/v1/534d8565e4b0c7f5e4fcb4f7/1562030061043-ICZGG34BMCXHR40HHXGX/ke17ZwdGBToddI8pDm48kFyD7pzB8zoMIVY5aiUuFlp7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0jG2lbcDYBOeMi4OFSYem8DMb5PTLoEDdB05UqhYu-xbnSznFxIRsaAU-3g5IaylIg/foster-supply-hospitality-ARNOLD-2019-06-Conservatory-Food-Scott-Yoga-Exteriors-Lawrence-Braun-0001-LB2_2700.jpg",
		"Description": "The Arnold House is a lively Catskills getaway located on Shandelee Mountain, near the quaint town of Livingston Manor. With our Tavern, newly renovated Barn & Greenhouse, expansive grounds & hiking trails and access to the area's storied outdoor activities our mission is to treat our guests to the comfort and relaxation of casual country living.",
		"Location": "Arnold House"
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
	global pictures
	global current_id

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
		poster=filename
		description=request.form["description"]
		location=request.form["location"]

		new_picture_entry={
			"Id": current_id,
			"Poster": url_for('static', filename='uploads/' + filename),
			"Description": description,
			"Location": location
		}
		current_id += 1
		pictures.append(new_picture_entry)
		flash('Image was uploaded successfully')
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