from flask import Flask, make_response, request
from markupsafe import escape
from flask import render_template
from flask import Response
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastro")
def cadastro():
    return render_template('usuario.html')

@app.route("/login")
def login():
    return render_template('cria_usuario.html')

@app.route("/anuncio")
def anuncio():
    return render_template('anuncio.html')

@app.route("/duvida")
def duvida():
    return render_template('duvida.html')

@app.route("/favoritos")
def favoritos():
    return render_template('favorito.html')

@app.route("/config/categoria")
def categoria():
    return render_template('categoria.html')

@app.route("/relatorio/venda")
def relvendas():
    return render_template('relvenda.html')

@app.route("/relatorio/compra")
def relcompra():
    return render_template('relcompra.html')