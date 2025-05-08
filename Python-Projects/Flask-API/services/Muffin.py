import os
import flask
from werkzeug.utils import secure_filename

from services.config import *
from services.view import imgProcessing

from typing import Dict


@app.route("/Muffin/",  methods=['POST'])
def Muffin()->str:
	return flask.render_template("./Muffin/Muffin.html")
	

@app.route("/Muffin/img",  methods=['GET','POST'])
def MuffinImg()->str:
	def allowed(filename:str)->bool:
		return '.' in filename and filename.rsplit('.',1)[1].lower() in IMG_ALLOWED
		
	def getOptions()->Dict[str, str]:
		opts = {}
		opts["MuffinImg"] = flask.request.form["MuffinImg"]
		opts["yogurt"] = flask.request.form["yogurt"]
		return opts
			
	if flask.request.method == 'POST':
		if "ImgMuffin" not in flask.request.files:
			return flask.redirect(flask.url_for("Muffin"))# flask.request.url
		file = flask.request.files["ImgMuffin"]
		if file.filename == '':
			return flask.redirect(flask.url_for("Muffin"))
			
		if file and allowed(file.filename):
			opts = getOptions()
	
			# generate hash of filename
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config["UPLOAD"], filename))
			
			img1 = os.path.join(app.config["UPLOAD"], filename)
			img2 = os.path.join(DATA, filename)
			imgProcessing(img1, img2, opts)
			
			return flask.redirect(flask.url_for("MuffinImgbis", img=filename))
	return flask.redirect(flask.url_for("Muffin"))

@app.route("/Muffin/<img>")
def MuffinImgbis(img:str)->str:
	#return flask.send_from_directory(app.config['UPLOAD'], img)
	return flask.send_from_directory(DATA, img)
