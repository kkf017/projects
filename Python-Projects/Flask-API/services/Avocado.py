import os
import flask
from werkzeug.utils import secure_filename

from services.config import *
from services.view import imgProcessing

from typing import Dict


@app.route("/Avocado/",  methods=['POST'])
def Avocado()->str:
	return flask.render_template("./Avocado/Avocado.html")


@app.route("/Avocado/img",  methods=['GET','POST'])
def AvocadoImg()->str:
	def allowed(filename:str)->bool:
		return '.' in filename and filename.rsplit('.',1)[1].lower() in IMG_ALLOWED
		
	def getOptions()->Dict[str, str]:
		opts = {}
		opts["AvocadoImg"] = flask.request.form["AvocadoImg"]
		opts["avocado21"] = flask.request.form["avocado21"]
		opts["avocado22"] = flask.request.form["avocado22"]
		return opts
			
	if flask.request.method == 'POST':
		if "ImgAvocado" not in flask.request.files:
			return flask.redirect(flask.url_for("Avocado"))# flask.request.url
		file = flask.request.files["ImgAvocado"]
		if file.filename == '':
			return flask.redirect(flask.url_for("Avocado"))

		if file and allowed(file.filename):
			opts = getOptions()
			
			# generate hash of filename
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config["UPLOAD"], filename))	
			
			img1 = os.path.join(app.config["UPLOAD"], filename)
			img2 = os.path.join(DATA, filename)
			imgProcessing(img1, img2, opts)
			
			return flask.redirect(flask.url_for("AvocadoImgbis", img=filename))
	return flask.redirect(flask.url_for("Avocado"))
	
	
@app.route("/Avocado/<img>")
def AvocadoImgbis(img:str)->str:
	#return flask.send_from_directory(app.config['UPLOAD'], img)
	return flask.send_from_directory(DATA, img)
