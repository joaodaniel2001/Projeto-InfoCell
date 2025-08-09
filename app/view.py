
# Importação das Bibliotecas
from app import app
from flask import render_template, url_for, request, redirect
from app.forms import UserForm, LoginForm
from flask_login import login_user, logout_user, current_user, login_required

# Tela inicial
@app.route ('/', methods=['GET', 'POST'])
def homepage ():
    return render_template ("index.html")

# Página de Cadastro
@app.route ('/cadastro', methods=['GET', 'POST'])
def Register ():
    form = UserForm ()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template ("cadastro.html", form=form)