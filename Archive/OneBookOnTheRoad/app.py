import flask

from services.config import * 
#from services.maps.calculation import *

from services.service.MapsService import *
from services.service.UserLoginService import *
from services.service.UserAccountService import *
from services.service.LocationService import *

#https://www.boites-a-livres.fr/
#https://boite.a.livres.zonelivre.fr/boites-a-livres-par-departements/

# manage PATH of app - in  config.py

# Finir navbar on small screen - for home, and user profil

# finir Login - verification email (login, change email...)

# Check create account / login - and manage errors

# Finir create account - chose your icon, ...etc

# Add email - verification

# Finir Forgot password

# RESTRUCT code - with comments (organize) - Revoir HTML code - avec import de code



# Add suppress account - user

# Create Footer

# Change the way people can give/suppress address of book boxes


@app.route("/")
def home()->str:
	# remove all files from ../static/maps	
	return flask.render_template("home.html")
	
	
@app.route("/unknown/", methods=['POST'])
def unknown()->str:
	return flask.render_template("unknown.html")	

	
if __name__ == "__main__":

	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
