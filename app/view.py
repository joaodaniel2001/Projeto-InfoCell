
from app import app
from app.forms import UserForm, LoginForm

from flask import render_template, url_for, request, redirect
from flask_login import login_user, logout_user, current_user, login_required

# Página Home
@app.route("/", methods=["GET", "POST"])
def Homepage ():
    return render_template ("index.html")

# Página de Login
@app.route ('/login', methods=['GET', 'POST'])
def LoginPage ():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.login ()
        login_user(user, remember=True)
        return redirect(url_for('Homepage'))
    return render_template ("login.html", form=form)

# Página de Produtos
@app.route ('/produtos', methods=['GET', 'POST'])
def Products ():
    return render_template ("produtos.html")

# Página de Sobre Nós
@app.route ('/sobre-nos', methods=['GET', 'POST'])
def AboutUs ():
    return render_template ("sobreNos.html")    

# Página de Cadastro
@app.route ('/cadastro', methods=['GET', 'POST'])
def Register ():
    form = UserForm ()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('Homepage'))
    return render_template ("cadastro.html", form=form)

# Deslogar
@app.route('/sair/')
@login_required
def logout ():
    logout_user()
    return redirect(url_for('Homepage'))