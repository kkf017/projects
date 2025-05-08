"""-----------------------------------------------------------------------------------------------------------------

            File that contains functions for Postit View.
                * Fix redirection - for @app.delete("/close/postits")

-----------------------------------------------------------------------------------------------------------------"""
import flask

from services.config import *
from services.Postit.PostitController import *


@app.route("/postit", methods=['GET'])
def getPostitView():
    """
    	Function to get a Postit (according to its uid and iid).
    	    URL:  http://127.0.0.1:8000/postit?uid=""&iid=""
    """
    iid = flask.request.args.get('iid')
    uid = flask.request.args.get('uid')
    value = getPostitController(uid, iid)
    return flask.jsonify({"resp": value})
    
    
@app.route("/postits", methods=['GET'])
def getPostitsView():
    """
    	Function to get all Postits (for a User).
    	    URL:  http://127.0.0.1:8000/postits?uid=""
    """
    uid = flask.request.args.get('uid')
    value = getPostitsController(uid)
    return flask.jsonify({"resp": value})


@app.route("/new", methods=['POST'])
def createPostitView():
    """
    	Function to create a Postit (for a User).
    	    URL:  http://127.0.0.1:8000/new
    """
    uid, title, time, memo, img = flask.request.json["uid"], flask.request.json["title"], flask.request.json["time"], flask.request.json["memo"], flask.request.json["img"]
    createPostitController(uid, title, time, memo, img)
    return flask.jsonify({"resp": True})
    
# (Not ok !)
@app.route("/close/postit", methods=['DELETE'])
def removePostitView():
    """
    	Function to remove a Postit (for a User).
    	    URL: http://127.0.0.1:8000/close/postit?uid=""&iid=""
    """
    iid = flask.request.args.get('iid')
    uid = flask.request.args.get('uid')
    value = removePostitController(uid, iid)
    return flask.jsonify({"resp": value})

@app.route("/close/postits", methods=['DELETE'])
def removePostits():
    """
    	Function to remove all Postits (for a User).
    	    URL: http://127.0.0.1:8000/close/postits?uid=""
    """
    uid = flask.request.args.get('uid')
    value = removePostitsController(uid)
    #print(request.url_for("closeAccount").include_query_params(uid=uid))
    #return RedirectResponse(request.url_for("closeAccount").include_query_params(uid=uid))
    return flask.jsonify({"resp": value})   
    
  
