import uvicorn
import gunicorn

from services.config import *
from services.User.UserModel import *
from services.Postit.PostitModel import *


from fastapi import Request, Form




@app.get("/")
def home(request: Request):
    return f"Hello"
	#return TEMPLATES.TemplateResponse(name="login.html", request=request)

	
	
if __name__ == '__main__':
    # uvicorn main:app --reload
	uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

