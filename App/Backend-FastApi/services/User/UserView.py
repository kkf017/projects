"""-----------------------------------------------------------------------------------------------------------------

            File that contains functions for User View.

-----------------------------------------------------------------------------------------------------------------"""

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, RedirectResponse

from pydantic import BaseModel

from services.config import *
from services.User.UserController import *


class User(BaseModel):
    uid: str = None
    email: str = None
    password: str = None
    value: str = None


@app.get("/user", response_class=JSONResponse)
def getUser(request:Request):
    """
    	Function to get a User (according to its uid).
    	    URL: http://127.0.0.1:8000/user?uid=""
    """
    uid = request.query_params['uid']
    value = getUserController(uid)
    return JSONResponse(content=value)



@app.post("/signup", response_class=JSONResponse)
def signup(user:User):
    """
    	Function to create a User (signup).
    	    URL: http://127.0.0.1:8000/signup
    """
    flag = createUserController(user.email, user.password)
    return JSONResponse(content={"flag": flag})


@app.post("/signin", response_class=JSONResponse)
def signin(user:User):
    """
    	Function to login (signin).
    	    URL: http://127.0.0.1:8000/signin
    """
    flag = loginUserController(user.email, user.password)
    return JSONResponse(content={"flag": flag})



@app.post("/update/email", response_class=JSONResponse)
def updateEmail(user:User):
    """
    	Function to update email (for a User).
    	    URL: http://127.0.0.1:8000/update/email
    """
    flag = updateEmailUserController(user.uid, user.value)
    return JSONResponse(content={"flag": flag})


@app.post("/update/password", response_class=JSONResponse)
def updatePassword(user:User):
    """
    	Function to update password (for a User).
    	    URL: http://127.0.0.1:8000//update/password
    """
    flag = updatePasswordUserController(user.uid, user.value)
    return JSONResponse(content={"flag": flag})



@app.delete("/close/account")
def closeAccount(request:Request):
    """
    	Function to close account (for a User).
    	    URL: http://127.0.0.1:8000/close/account?uid=""
    """
    uid = request.query_params['uid']
    flag = removeUserController(uid)
    # remove all Postits - for a user
    #return JSONResponse(content= {"flag": flag})


