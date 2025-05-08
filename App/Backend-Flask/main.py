import os
import flask

from services.config import *
from services.User.UserModel import *
from services.Postit.PostitModel import *



@app.route("/")
def home():
    return f"Hello, from Flask App."

	
	
if __name__ == '__main__':
	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))

