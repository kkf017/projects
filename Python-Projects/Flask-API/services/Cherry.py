import os
import flask
from werkzeug.utils import secure_filename

from services.config import *
from services.view import imgProcessing

from typing import Dict

@app.route("/Cherry/",  methods=['POST'])
def Cherry()->str:
	return flask.render_template("./Cherry/Cherry.html")
	
@app.route("/Cherry/img",  methods=['GET','POST'])
def CherryImg()->str:
	def allowed(filename:str)->bool:
		return '.' in filename and filename.rsplit('.',1)[1].lower() in IMG_ALLOWED
		
	def getOptions()->Dict[str, str]:
		opts = {}
		opts["CherryImg"] = flask.request.form["CherryImg"]
		opts["cherry1x"] = flask.request.form["cherry1x"]
		opts["cherry1y"] = flask.request.form["cherry1y"]
		opts["cherry1width"] = flask.request.form["cherry1width"]
		opts["cherry1height"] = flask.request.form["cherry1height"]
		opts["cherry2angl"] = flask.request.form["cherry2angl"]
		opts["cherry3z"] = flask.request.form["cherry3z"]
		return opts
			
	if flask.request.method == 'POST':
		if "ImgCherry" not in flask.request.files:
			return flask.redirect(flask.url_for("Cherry"))# flask.request.url
		file = flask.request.files["ImgCherry"]
		if file.filename == '':
			return flask.redirect(flask.url_for("Cherry"))
			
		if file and allowed(file.filename):
			opts = getOptions()
	
			# generate hash of filename
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config["UPLOAD"], filename))	
			
			img1 = os.path.join(app.config["UPLOAD"], filename)
			img2 = os.path.join(DATA, filename)
			imgProcessing(img1, img2, opts)
			
			return flask.redirect(flask.url_for("CherryImgbis", img=filename))
	return flask.redirect(flask.url_for("Cherry"))
	
	
@app.route("/Cherry/<img>")
def CherryImgbis(img:str)->str:
	#return flask.send_from_directory(app.config['UPLOAD'], img)
	return flask.send_from_directory(DATA, img)
