import os
import flask
from werkzeug.utils import secure_filename

from services.config import *
from services.view import imgProcessing

from typing import Dict


@app.route("/Cookie/",  methods=['POST'])
def Cookie()->str:
	return flask.render_template("./Cookie/Cookie.html")


@app.route("/Cookie/img",  methods=['GET','POST'])
def CookieImg()->str:
	def allowed(filename:str)->bool:
		return '.' in filename and filename.rsplit('.',1)[1].lower() in IMG_ALLOWED
		
	def getOptions()->Dict[str, str]:
		opts = {}
		opts["CookieImg"] = flask.request.form["CookieImg"]
		opts["donut"] = flask.request.form["donut"]
		opts["crunchy1"] = flask.request.form["crunchy1"]
		opts["crunchy2"] = flask.request.form["crunchy2"]
		opts["cheesecake1"] = flask.request.form["cheesecake1"]
		opts["cheesecake2"] = flask.request.form["cheesecake2"]		
		opts["choconuts"] = flask.request.form["choconuts"]
		opts["candypop"] = flask.request.form["candypop"]
		opts["sugar"] = flask.request.form["sugar"]
		
		for i in range(1,5):
			opts[f"cone{i}"] = flask.request.form[f"cone{i}"]			
			opts[f"rainbow{i}"] = flask.request.form[f"rainbow{i}"]			
			opts[f"icecream{i}"] = flask.request.form[f"icecream{i}"]
		
		return opts
			
	if flask.request.method == 'POST':
		if "ImgCookie" not in flask.request.files:
			return flask.redirect(flask.url_for("Cookie"))# flask.request.url
		file = flask.request.files["ImgCookie"]
		if file.filename == '':
			return flask.redirect(flask.url_for("Cookie"))	
		if file and allowed(file.filename):
			opts = getOptions()
			
			# generate hash of filename
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config["UPLOAD"], filename))	
			
			img1 = os.path.join(app.config["UPLOAD"], filename)
			img2= os.path.join(DATA, filename)
			imgProcessing(img1, img2, opts)
			
			return flask.redirect(flask.url_for("CookieImgbis", img=filename))
	return flask.redirect(flask.url_for("Cookie"))
	
	
@app.route("/Cookie/<img>")
def CookieImgbis(img:str)->str:
	#return flask.send_from_directory(app.config['UPLOAD'], img)
	return flask.send_from_directory(DATA, img)
