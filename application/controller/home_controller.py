from flask import render_template
from application.model.dao.produto_dao import Produto_dao
from application import app

@app.route('/',methods=['GET'])
def home():
    produtos_lista = Produto_dao().produtos_list()
    return render_template("home.html", produtos_lista = produtos_lista)