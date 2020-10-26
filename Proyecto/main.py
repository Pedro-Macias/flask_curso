# ARCHIVO DE INICIO
from flask import Flask 
from flask import render_template
from flask import request
from flask_wtf import CsrfProtect
import forms


app = Flask(__name__) 
# vamos a ponerle una clave secreta , para validar ataques externos
app.secret_key = 'mi_clave_secreta'
csrf = CsrfProtect(app)


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
 
@app.route('/login',methods = ['GET', 'POST'])
def login():
    login_form = forms.LoginForm()
    title = 'formulario login'
    return render_template('login.html',title=title ,form= login_form)        
        



    

if __name__ == '__main__':
    app.run(debug= True,port= 8000)