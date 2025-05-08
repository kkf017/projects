"""-----------------------------------------------------------------------------------------------------------------

            File that contains functions for Postit View.
                * Fix redirection - for @app.delete("/close/postits")

-----------------------------------------------------------------------------------------------------------------"""

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, RedirectResponse

from pydantic import BaseModel

from services.config import *
from services.Postit.PostitController import *


# raise HTTPException(status_code=404, detail="Hero not found")


class Postit(BaseModel):
    uid: str = None
    title: str = None
    time: str = None
    memo: str = None
    img: str = None




@app.get("/postit", response_class=JSONResponse)
def getPostit(request:Request):
    """
    	Function to get a Postit (according to its uid and iid).
    	    URL:  http://127.0.0.1:8000/postit?uid=""&iid=""
    """
    iid = request.query_params['iid']
    uid = request.query_params['uid']
    value = getPostitController(uid, iid)
    return JSONResponse(content=value)


@app.get("/postits", response_class=JSONResponse)
def getPostit(request:Request):
    """
    	Function to get all Postits (for a User).
    	    URL:  http://127.0.0.1:8000/postits?uid=""
    """
    uid = request.query_params['uid']
    value = getPostitsController(uid)
    return JSONResponse(content=value)


@app.post("/new")
def createPostit(postit:Postit):
    """
    	Function to create a Postit (for a User).
    	    URL:  http://127.0.0.1:8000/new
    """
    createPostitController(postit.uid, postit.title, postit.time, postit.memo, postit.img)


@app.delete("/close/postit")
def removePostit(request:Request):
    """
    	Function to remove a Postit (for a User).
    	    URL: http://127.0.0.1:8000/close/postit?uid=""&iid=""
    """
    iid = request.query_params['iid']
    uid = request.query_params['uid']
    flag = removePostitController(uid, iid)
    #return JSONResponse(content=value)


@app.delete("/close/postits")
def removePostits(request:Request):
    """
    	Function to remove all Postits (for a User).
    	    URL: http://127.0.0.1:8000/suppress/postit?uid=""
    """
    uid = request.query_params['uid']
    flag = removePostitsController(uid)
    #print(request.url_for("closeAccount").include_query_params(uid=uid))
    return RedirectResponse(request.url_for("closeAccount").include_query_params(uid=uid))


