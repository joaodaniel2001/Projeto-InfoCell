
# Importação das Bibliotecas
from flask import render_template, url_for, request, redirect
from flask_login import login_user, logout_user, current_user, login_required

# Importação de outras Pastas
from app import app

# Página Inicial
@app.route("/", methods=["GET", "POST"])
def homepage():
    return render_template("index.html")