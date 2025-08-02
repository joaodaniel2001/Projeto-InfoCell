
# Importação das Bibliotecas
from app import app
from flask import render_template

@app.route ('/', methods=['GET', 'POST'])
def homepage ():
    return render_template ("index.html")
