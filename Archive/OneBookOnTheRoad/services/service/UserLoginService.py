import flask

from services.config import * 
import services.users.management


###################################################################################################################

@app.route("/log/", methods=['GET','POST'])
def log()->str:	
	return flask.redirect(flask.url_for("login"))
	

@app.route("/login/", methods=['GET','POST'])
def login()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/login/
	"""
	if flask.request.method == 'POST':
		email = flask.request.form["Email"]
		password = flask.request.form["password"]
		flag = services.users.management.loginUser(email, password)
		if flag == "":
			return flask.render_template(os.path.join(TEMPLATE, "/login/login.html"), msg="Email, or password not valid.")
			
		# add forget your password ?
		return flask.redirect(flask.url_for("user", idt=flag))
		 
	return flask.render_template(os.path.join(TEMPLATE, "/login/login.html"), msg="")

	
@app.route("/user/<idt>", methods=['GET','POST'])
def user(idt:str)->str:
	""" 
		(URL):
			http://127.0.0.1:5000/user/daaab105702e8d6ffd23ad6f0f7a50de4c0eda8b
	"""
	user = {}
	user["hash"] = idt
	#user = getUserInfo(idt)
	return flask.render_template("home-profil.html", user=user)


##################################################################################################################	


@app.route("/registration/", methods=['POST'])
def registration()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/register/
	"""
	return flask.redirect(flask.url_for("register")) 


@app.route("/register/", methods=['GET','POST'])
def register()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/register/
	"""
	def check():
		pass
	
	if flask.request.method == 'POST':	
		username = flask.request.form["Username"]
		email = flask.request.form["Email"]
		password = flask.request.form["password"]
		check = flask.request.form["password-check"]
		
		if services.users.management.exists("Email", email, username):
			return flask.render_template(os.path.join(TEMPLATE, "/login/register.html"), msg="An account already exists.")
		
		if services.users.management.exists("Email", email):
			return flask.render_template(os.path.join(TEMPLATE, "/login/register.html"), msg="This email is already used.")
		
		if services.users.management.exists("Username", username):
			return flask.render_template(os.path.join(TEMPLATE, "/login/register.html"), msg="This username is already used.")
			
		if not (password == check):
			return flask.render_template(os.path.join(TEMPLATE, "/login/register.html"), msg="Password is not valid.")
		
		# add password verification - at least one upper, one digit, one symbol
			# https://www.geeksforgeeks.org/password-validation-in-python/
			
		# add email verification
		
		# add to database
		services.users.management.createUser(email, username, password)
		return flask.render_template("unknown.html", msg="")
	return flask.render_template(os.path.join(TEMPLATE, "/login/register.html"), msg="")
	

###################################################################################################################

@app.route("/logout/", methods=['GET','POST'])
def logout()->str:
	""" 
		(URL):
			http://
	"""
	return flask.redirect(flask.url_for("log"))	
	




