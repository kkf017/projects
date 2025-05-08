"""-----------------------------------------------------------------------------------------------------------------

            File that contains functions for User View.

-----------------------------------------------------------------------------------------------------------------"""
import flask

from services.config import *
from services.User.UserController import *


@app.route("/user", methods=['GET'])
def getUserView():
    """
    	Function to get a User (according to its uid).
    	    URL: http://127.0.0.1:8000/user?uid=""
    """
    uid = flask.request.args.get('uid')
    value = getUserController(uid)
    return flask.jsonify({"resp": value})
    

@app.route("/signup", methods=['POST'])
def createUserView():
    """
    	Function to create a User (signup).
    	    URL: http://127.0.0.1:8000/signup
    """
    email, password = flask.request.json["email"], flask.request.json["password"]
    value = createUserController(email, password)
    return flask.jsonify({"resp": value})
    
    

@app.route("/signin", methods=['POST'])
def loginUserView():
    """
    	Function to login (signin).
    	    URL: http://127.0.0.1:8000/signin
    """
    email, password = flask.request.json["email"], flask.request.json["password"]
    value = loginUserController(email, password)
    return flask.jsonify({"resp": value})
    
    
@app.route("/update/email", methods=['POST'])
def updateEmailUserView():
    """
    	Function to update email (for a User).
    	    URL: http://127.0.0.1:8000/update/email
    """
    uid, email = flask.request.json["uid"], flask.request.json["email"]
    value = updateEmailUserController(uid, email)
    return flask.jsonify({"resp": value})
    

@app.route("/update/password", methods=['POST'])
def updatePasswordUserView():
    """
    	Function to update password (for a User).
    	    URL: http://127.0.0.1:8000//update/password
    """
    uid, password = flask.request.json["uid"], flask.request.json["password"]
    value = updatePasswordUserController(uid, password)
    return flask.jsonify({"resp": value})
    

@app.route("/close/account",  methods=['DELETE'])
def removeUserView():
    """
    	Function to close account (for a User).
    	    URL: http://127.0.0.1:8000/close/account?uid=""
    """
    uid = flask.request.args.get('uid')
    value = removeUserController(uid)
    # remove all Postits - for a user
    return flask.jsonify({"resp": value})
