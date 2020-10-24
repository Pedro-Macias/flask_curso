# ARCHIVO DE INICIO
from flask import Flask 
from flask import render_template
from flask_wtf import FlaskForm
import forms

app = Flask(__name__) 
@app.route('/') 
def index():
    formulario_coment = forms.ComentarioForm()
    title = 'Mi Proyecto Flask'
    return render_template('index.html',title=title, form =formulario_coment )

    

if __name__ == '__main__':
    app.run(debug= True,port= 8000)