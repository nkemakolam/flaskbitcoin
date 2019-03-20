from flask import render_template
from flask import request
from app import app
import processed_data

@app.route('/',methods = ['GET'])

def index():
    return render_template("index.html", data = processed_data.get_data())


