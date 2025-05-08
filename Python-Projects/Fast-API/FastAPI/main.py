import uvicorn

from services.config import *

# REVOIR - (clean code)
# uvicorn main:app --reload
	
	
if __name__ == '__main__':
	uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)	
