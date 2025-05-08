from fastapi import Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse

from services.config import *
from services.Nasa.nasa import *


		
@app.post("/reload", response_class=RedirectResponse)
def reload(request: Request):
	IMAGES.get_IMG(N)
	return RedirectResponse(request.url_for("home"))
	

@app.post("/search", response_class=HTMLResponse)
def search(request: Request, dateFrom = Form(...), dateTo = Form(...)):
	img = IMAGES.select(dateFrom, dateTo)
	return TEMPLATES.TemplateResponse(name="nav-1.html", request={"request":request, "value":img})
		

@app.post("/photo", response_class=HTMLResponse)
def profil(request: Request):
	img = IMAGES.get_image(request.query_params['id'])
	return TEMPLATES.TemplateResponse(request={"request":request, "value":img}, name="profil.html")	
	

@app.get("/", response_class=HTMLResponse)
@app.post("/", response_class=HTMLResponse)
def home(request: Request):
	return TEMPLATES.TemplateResponse(name="nav-1.html", request={"request":request, "value":IMAGES.images})


"""
@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
	return TEMPLATES.TemplateResponse(name="login.html", request=request)
"""
