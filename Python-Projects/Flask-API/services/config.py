import os
import flask

PATH = "/home/User/Documents/app1" # path of your app


IMG_ALLOWED = {'png', 'jpg', 'jpeg', 'JPG'}#'JPG', 'gif'}

TEMPLATE = f"{PATH}/template"
STATIC = f"{PATH}/static"
DATA = f"{PATH}/static/data"

app = flask.Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)
app.config['UPLOAD'] = os.path.join(STATIC, 'upload')
