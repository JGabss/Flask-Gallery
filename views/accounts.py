from flask import render_template, request, redirect, session, url_for, flash
from app import app, db
from models import User

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        usuario = User.query.filter_by(username=request.form['usuario']).first()
        if usuario:
            if request.form['senha'] == usuario.senha:
                session['usuario_logado'] = usuario.username
                flash(usuario.username + ' logado com sucesso!')
                proxima_pagina = request.form['proxima']
                return redirect(proxima_pagina)
            else:
                flash('Usuário não logado!')
                return redirect(url_for('login'))
        else:
            flash('Usuário não logado!')
            return redirect(url_for('login'))
    
    proxima = request.args.get("proxima")
    return render_template('accounts/login.html', proxima=proxima, titulo='Login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect(url_for('index'))

@app.route("/create", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nome = request.form["nome"]
        username = request.form["usuario"]
        senha = request.form["senha"]

        if User.query.filter_by(username=username).first():
            flash("Ihhh, Usuário já cadastrado")
            return redirect(url_for("index"))


        new_user = User(nome=nome, username=username, senha=senha)
        new_user.create(nome=nome, username=username, senha=senha)

        flash("Usuário cadastrado com sucesso")

        return redirect(url_for("login"))

    return render_template("accounts/register.html", titulo="Novo Usuário")

