import os
import flask
from werkzeug.utils import secure_filename

from services.config import *
from services.view import imgProcessing

from typing import Dict



@app.route("/Coffee/",  methods=['POST'])
def Coffee()->str:
	return flask.render_template("./Coffee/Coffee.html")
	
	

@app.route("/Coffee/img",  methods=['GET','POST'])
def CoffeeImg()->str:
	def allowed(filename:str)->bool:
		return '.' in filename and filename.rsplit('.',1)[1].lower() in IMG_ALLOWED
		
	def getOptions()->Dict[str, str]:
		opts = {}
		opts["CoffeeImg"] = flask.request.form["CoffeeImg"]
		opts["coffee21"] = flask.request.form["coffee21"]
		opts["coffee22"] = flask.request.form["coffee22"]
		
		opts["coffee31"] = flask.request.form["coffee31"]
		opts["coffee32"] = flask.request.form["coffee32"]
		opts["coffee33"] = flask.request.form["coffee33"]
		return opts
			
	if flask.request.method == 'POST':
		if "ImgCoffee" not in flask.request.files:
			return flask.redirect(flask.url_for("Coffee"))# flask.request.url
		file = flask.request.files["ImgCoffee"]
		if file.filename == '':
			return flask.redirect(flask.url_for("Coffee"))
			
		if file and allowed(file.filename):
			opts = getOptions()
			
			# generate hash of filename
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config["UPLOAD"], filename))	
			
			# image processing
			img1 = os.path.join(app.config["UPLOAD"], filename)
			img2 = os.path.join(DATA, filename)
			imgProcessing(img1, img2, opts)
			
			return flask.redirect(flask.url_for("CoffeeImgbis", img=filename))
	return flask.redirect(flask.url_for("Coffee"))
	
	
@app.route("/Coffee/<img>")
def CoffeeImgbis(img:str)->str:
	#return flask.send_from_directory(app.config['UPLOAD'], img)
	return flask.send_from_directory(DATA, img)
