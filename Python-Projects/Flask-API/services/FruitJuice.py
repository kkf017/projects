import os
import flask
from werkzeug.utils import secure_filename

from services.config import *
from services.view import imgProcessing

from typing import Dict


@app.route("/FruitJuice/",  methods=['POST'])
def FruitJuice()->str:
	return flask.render_template("./FruitJuice/FruitJuice.html")

	
@app.route("/FruitJuice/img",  methods=['GET','POST'])
def FruitJuiceImg()->str:
	def allowed(filename:str)->bool:
		return '.' in filename and filename.rsplit('.',1)[1].lower() in IMG_ALLOWED
		
	def getOptions()->Dict[str, str]:
		opts = {}
		opts["FruitJuiceImg"] = flask.request.form["FruitJuiceImg"]
		opts["blueberry1"] = flask.request.form["blueberry1"]
		opts["blueberry2"] = flask.request.form["blueberry2"]
		opts["lemon"] = flask.request.form["lemon"]
		return opts
			
	if flask.request.method == 'POST':
		if "ImgFruitJuice" not in flask.request.files:
			return flask.redirect(flask.url_for("FruitJuice"))# flask.request.url
		file = flask.request.files["ImgFruitJuice"]
		if file.filename == '':
			return flask.redirect(flask.url_for("FruitJuice"))
			
		if file and allowed(file.filename):
			opts = getOptions()
	
			# generate hash of filename
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config["UPLOAD"], filename))	
			
			# image processing
			img1 = os.path.join(app.config["UPLOAD"], filename)
			img2 = os.path.join(DATA, filename)
			imgProcessing(img1, img2, opts)
			
			return flask.redirect(flask.url_for("FruitJuiceImgbis", img=filename))
	return flask.redirect(flask.url_for("FruitJuice"))
	
	
@app.route("/FruitJuice/<img>")
def FruitJuiceImgbis(img:str)->str:
	#return flask.send_from_directory(app.config['UPLOAD'], img)
	return flask.send_from_directory(DATA, img)
