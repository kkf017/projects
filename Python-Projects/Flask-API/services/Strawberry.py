import os
import flask
from werkzeug.utils import secure_filename

from services.config import *
from services.view import imgProcessing

from typing import Dict


	
@app.route("/Strawberry/",  methods=['POST'])
def Strawberry()->str:
	return flask.render_template("./Strawberry/Strawberry.html")
	
@app.route("/Strawberry/img",  methods=['GET','POST'])
def StrawberryImg()->str:
	def allowed(filename:str)->bool:
		return '.' in filename and filename.rsplit('.',1)[1].lower() in IMG_ALLOWED
		
	def getOptions()->Dict[str, str]:
		opts = {}
		opts["StrawberryImg"] = flask.request.form["StrawberryImg"]
		
		if opts["StrawberryImg"] == "cupoftea":
			if "ImgStrawberrybis" not in flask.request.files:
				return flask.redirect(flask.url_for("Strawberry"))# flask.request.url
			file = flask.request.files["ImgStrawberrybis"]
			if file.filename == '':
				return flask.redirect(flask.url_for("Strawberry"))
			if file and allowed(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config["UPLOAD"], filename))
				opts["cupoftea"] = os.path.join(app.config["UPLOAD"], filename)
		return opts
			
	if flask.request.method == 'POST':
		if "ImgStrawberry" not in flask.request.files:
			return flask.redirect(flask.url_for("Strawberry"))# flask.request.url
		file = flask.request.files["ImgStrawberry"]
		if file.filename == '':
			return flask.redirect(flask.url_for("Strawberry"))
			
		if file and allowed(file.filename):
			opts = getOptions()
	
			# generate hash of filename
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config["UPLOAD"], filename))	
			
			img1 = os.path.join(app.config['UPLOAD'], filename)
			img2 = os.path.join(DATA, filename)
			imgProcessing(img1, img2, opts)
			
			return flask.redirect(flask.url_for("StrawberryImgbis", img=filename))
	return flask.redirect(flask.url_for("Strawberry"))
	
	
@app.route("/Strawberry/<img>")
def StrawberryImgbis(img:str)->str:
	#return flask.send_from_directory(app.config['UPLOAD'], img)
	return flask.send_from_directory(DATA, img)
		
