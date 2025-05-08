import os
import flask

from services.config import *
import services.maps.calculation

from typing import Dict, Any

#################################################################################################################

def location(uid:str, addr:str, radius:float)->Dict[str, Any]:
	value = {}
	value["uid"] = uid
	value["result"] = services.maps.calculation.sphere(addr, radius)
	return value
	
def place(uid:str, ids:str)->Dict[str, Any]:
	value = {}
	value["uid"] = uid
	value["result"] = services.maps.calculation.searchID(ids)
	return value

@app.route("/location/", methods=['GET','POST'])
def location1()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/location/
	"""		
	if flask.request.method == 'POST':	
		value = location(None, flask.request.form["search-addr"], float(flask.request.form["search-radius"]))		
	return flask.render_template(os.path.join(TEMPLATE, "/home/location.html"), value = value)
	

@app.route("/location", methods=['GET','POST'])
def location2()->str:	
	""" 
		(URL):
			http://127.0.0.1:5000/location?uid=daaab105702e8d6ffd23ad6f0f7a50de4c0eda8b
	"""	
	uid = flask.request.args.get('uid')
	
	if flask.request.method == 'POST':
		value = location(uid, flask.request.form["search-addr"], float(flask.request.form["search-radius"]))
	
	if uid != None:
		return flask.render_template(os.path.join(TEMPLATE, "/profil/profil-location.html"), value = value)
		
	return flask.render_template(os.path.join(TEMPLATE, "/profil/location.html"), value = value)
	
		
@app.route("/location/place", methods=['POST'])
def location3()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/location/place?id=3195b8f9e15dca563ba12d61e7dc576444db0218
	"""
	value = place(None, flask.request.args.get('id'))
	return flask.render_template(os.path.join(TEMPLATE, "/home/place.html"), value = value)	
	

@app.route("/place", methods=['GET','POST'])
def location4()->str:
	"""
		(URL):
			http://127.0.0.1:5000/place?uid=daaab105702e8d6ffd23ad6f0f7a50de4c0eda8b&id=3195b8f9e15dca563ba12d61e7dc576444db0218 
	"""
	uid = flask.request.args.get('uid')
	value = place(uid, flask.request.args.get('id'))
	value["id"] = flask.request.args.get('id')
	if uid != None:
		print(f"LOCATION4")
		return flask.render_template(os.path.join(TEMPLATE, "/profil/profil-place.html"), value = value)
	return flask.render_template(os.path.join(TEMPLATE, "/home/place.html"), value = value)
		

##################################################################################################################

def filt(uid:str, key:str, value:str)->Dict[str, Any]:
	res = {}
	res["uid"] = uid
	res["result"] = services.maps.calculation.filters(key, value)
	return res


@app.route("/search/", methods=['GET','POST']) # search
def search()->str:
	"""
		(URL):
			http://127.0.0.1:5000/search/
			http://127.0.0.1:5000/search/?uid=daaab105702e8d6ffd23ad6f0f7a50de4c0eda8b 
	"""
	result = {}
	#if flask.request.method == 'POST':	
		#result = fill()
	uid = flask.request.args.get('uid')
	value = {}
	value["uid"] = uid
	value["result"] = result	
	if uid != None:
		return flask.render_template(os.path.join(TEMPLATE, "/profil/profil-search.html"), value = value)
	return flask.render_template(os.path.join(TEMPLATE, "/home/search.html"), value = value)	


@app.route("/request/", methods=['GET','POST'])
def request()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/request/ 
	"""
	uid = flask.request.args.get('uid')	
	key, value = (None, None)

	if not flask.request.form["filter-country"] == "None":
		key, value = ("Country", flask.request.form["filter-country"])

	if not flask.request.form["filter-region"] == "None":
		key, value = ("Region", flask.request.form["filter-region"])	
		
	if not flask.request.form["filter-department"] == "None":
		key, value = ("Department", flask.request.form["filter-department"])	
	
	if not flask.request.form["filter-town"] == "None":
		key, value = ("Town", flask.request.form["filter-town"])

	value = filt(uid, key, value)		
	return flask.render_template(os.path.join(TEMPLATE, "/home/request.html"), value = value)
	

@app.route("/request", methods=['GET','POST'])
def request1()->str:
	"""
		(URL):	
	"""	
	uid = flask.request.args.get('uid')
	key, value = (None, None)

	if not flask.request.form["filter-country"] == "None":
		key, value = ("Country", flask.request.form["filter-country"])

	if not flask.request.form["filter-region"] == "None":
		key, value = ("Region", flask.request.form["filter-region"])	
		
	if not flask.request.form["filter-department"] == "None":
		key, value = ("Department", flask.request.form["filter-department"])	
	
	if not flask.request.form["filter-town"] == "None":
		key, value = ("Town", flask.request.form["filter-town"])

	value = filt(uid, key, value)
	if uid != None:
		return flask.render_template(os.path.join(TEMPLATE, "/profil/profil-request.html"), value = value)
	return flask.render_template(os.path.join(TEMPLATE, "/home/request.html"), value = value)
	

	
@app.route("/request/place", methods=['POST'])
def request2()->str:
	"""
		(URL):	
			http://127.0.0.1:5000/request/place?id=9c9d3793bf96ac5dad9d126ce5b68110d36a06ba
	"""
	value = place(None, flask.request.args.get('id'))
	return flask.render_template(os.path.join(TEMPLATE, "/home/place.html"), value = value)
	

###################################################################################################################

@app.route("/contact", methods=['GET','POST'])
@app.route("/contact/", methods=['GET','POST'])
def contact()->str:
	"""
		(URL):	
			http://127.0.0.1:5000/contact/
	"""
	uid = ""
	if flask.request.args.get('uid') != None:
		uid = flask.request.args.get('uid')
		return flask.render_template("./profil/profil-contact.html", uid=uid)
	return flask.render_template(os.path.join(TEMPLATE, "/home/contact.html"), uid=uid)
	
@app.route("/send/", methods=['POST'])
def send()->str:
	"""
		(URL):	
	"""
	return flask.render_template("unknown.html")
	

###################################################################################################################

