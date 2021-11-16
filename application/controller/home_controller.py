from flask import render_template
from application import app

@app.route('/',methods=['GET'])
def index():
    return render_template("home.html")