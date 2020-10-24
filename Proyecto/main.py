# ARCHIVO DE INICIO
from flask import Flask 
from flask import render_template

from flask import request

import forms


app = Flask(__name__) 
# las rutas son accedidas por metodo GET , si queremos otro metodo habra que indicarlo
@app.route('/', methods = ['GET', 'POST'] ) 
def index():
    formulario_coment = forms.ComentarioForm(request.form)
    if request.method == 'POST' and formulario_coment.validate():
        usu= formulario_coment.usuario.data
        mail = formulario_coment.email.data
        coment = formulario_coment.comentario.data
        return 'usuario: {} , email {} , comentario {}'.format(usu , mail , coment)
        
        

    title = 'Mi Proyecto Flask'
    return render_template('index.html',title=title, form =formulario_coment )

    

if __name__ == '__main__':
    app.run(debug= True,port= 8000)