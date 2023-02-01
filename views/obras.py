from flask import render_template, request, redirect, session, url_for
from app import app, db
from models import Obras
import openai
from decouple import config as ENV

@app.route("/", methods=["GET"])
def index():
    try:
        user = session["usuario_logado"]
    except:
        user = None

    obras = Obras.query.order_by(Obras.id)
    return render_template("obras/obras.html", obras=obras, user=user, titulo="Artes", exists=(True if len(obras.all()) > 0 else False))

@app.route("/nova_obra", methods=["GET", "POST"])
def new_art():
    try:
        user = session["usuario_logado"]
    
    except:
        return redirect(url_for("login", proxima=url_for("new_art")))

    if request.method == "POST":
        nome = request.form["nome"]
        autor = request.form["autor"]
        ano = request.form["ano"]
        conteudo = request.form["imagem"]

        openai.api_key = ENV("API_KEY")
        image = openai.Image.create(
            prompt=conteudo,
            n=1,
            size="512x512",
        )

        image_url = image["data"][0]["url"]

        Obras(nome=nome, autor=autor, ano_criacao=ano, propietario=session["usuario_logado"], url=conteudo)
        Obras.create(nome, autor, ano, session["usuario_logado"], image_url)

        return redirect(url_for("index"))



    return render_template("obras/nova_arte.html", user=user)

@app.route("/minhas_obras", methods=["GET"])
def my_arts():
    try:
        user = session["usuario_logado"]
    except:
        return redirect(url_for("login", proxima=url_for("my_arts")))


    obras = Obras.query.filter_by(propietario=user)
    return render_template("obras/minhas_obras.html", titulo="Minhas Artes", obras=obras, user=user, exists=(True if len(obras.all()) > 0 else False))

@app.route("/deletar/<int:id>")
def delete(id: int):
    try:
        user = session["usuario_logado"]
    except:
        return redirect(url_for("login", proxima=url_for("my_arts")))

    if Obras.query.filter_by(id=id).first().propietario == user:
        Obras.query.filter_by(id=id).delete()
        db.session.commit()

    return redirect(url_for("my_arts"))

@app.route("/atualizar/<int:id>", methods=["POST", "GET"])
def update(id: int):
    try:
        user = session["usuario_logado"]
    except:
        return redirect(url_for("login", proxima=url_for("my_arts")))
    
    if Obras.query.filter_by(id=id).first().propietario != user:
        return redirect(url_for("my_arts"))

    arte = Obras.query.filter_by(id=id).first()
    if request.method == "POST":
        arte.nome = request.form["nome"]
        arte.autor = request.form["autor"]
        arte.ano = request.form["ano"]

        db.session.add(arte)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("obras/editar.html", titulo="Editar", obra=arte, user=user)

@app.route("/sobre_nos/", methods=["GET"])
def about_us():
    try:
        user = session["usuario_logado"]
    except:
        user = None

    return render_template("sobre_nos.html", titulo="Sobre Nós", user=user )