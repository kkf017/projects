import flask

from services.config import * 
import services.users.management

@app.route("/place/like", methods=['GET','POST'])
def place1()->str:
	uid = flask.request.args.get('uid')
	ids = flask.request.args.get('id')
	# check if favorite is already in database
	if not services.users.management.exist(ids, uid):
		services.users.management.favorites(uid, ids)
	return flask.redirect(flask.url_for("location4", uid = flask.request.args.get('uid'), id = ids))


@app.route("/place/trade", methods=['GET','POST'])
def place2()->str:
	value = {}
	value["uid"] = flask.request.args.get('uid')
	value["ids"] = flask.request.args.get('id')
	value["color"] = "w3-purple"
	return flask.render_template(os.path.join(TEMPLATE, "/profil/profil-trade.html"), value = value)
	
	
"""
	uid id ask/exchange comment 12/06/2024
	
	clean requests - with periods
"""
