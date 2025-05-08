import os
import flask

from services.config import *
from services.FruitJuice import *
from services.Cherry import *
from services.Muffin import *
from services.Strawberry import *
from services.Avocado import *
from services.Cookie import *
from services.Coffee import *
from services.Soda import *




@app.route("/restart")
def restart()->str:

	folder = os.path.join(STATIC,"upload")
	for f in os.listdir(folder):
		print(os.path.join(folder, f))
		os.remove(os.path.join(folder, f))
	
	folder = os.path.join(STATIC,"data")
	for f in os.listdir(folder):
		print(os.path.join(folder, f))
		os.remove(os.path.join(folder, f))
			
	return flask.redirect(flask.url_for("home"))


@app.route("/")
def home()->str:	
	return flask.render_template("nav-3.html")
	

if __name__ == "__main__":

	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
	
	
	
