import os
import flask
from werkzeug.utils import secure_filename

from services.config import *

from typing import Dict


@app.route("/Soda/",  methods=['POST'])
def Soda()->str:
	return flask.render_template("./Soda/Soda.html")
