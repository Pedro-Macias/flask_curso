# ARCHIVO DE INICIO
from flask import Flask 
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import flash

from config import DevelopmetConfig

from flask import url_for
from flask import redirect
from flask_wtf import CsrfProtect

import forms
import json

app = Flask(__name__)
# aqui importamos el entorno que nos interese del config 
app.config.from_object(DevelopmetConfig)

# vamos a ponerle una clave secreta , para validar ataques externos
csrf = CsrfProtect()

# plantilla de error - el 404 es cuando el servidor no encuentra el recurso
@app.errorhandler(404)
def page_not_foud(error):
    title = 'error 404'
    return render_template('/404.html',title=title),404

# las rutas son accedidas por metodo GET , si queremos otro metodo habra que indicarlo
@app.route('/', methods = ['GET', 'POST'] ) 
def index():
    if 'username' in session:
        username = session['username']
        
    custome_cookie = request.cookies.get('custome_cookie','Undefined')
    

    title = 'Mi Proyecto Flask'
    return render_template('index.html',title=title)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

@app.route('/login',methods = ['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    title = 'formulario login'
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        sucess_message = 'Bienvenido {}'.format(username)
        flash(sucess_message)
        
        session['username'] = login_form.username.data
    return render_template('login.html', form= login_form, title=title)   

# hacemos una cookie
@app.route('/cookie')
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custome_cookie','Pedro')
    return response     

@app.route('/coment', methods = ['GET', 'POST'] ) 
def coment():
    if 'username' in session:
        username = session['username']
        
    custome_cookie = request.cookies.get('custome_cookie','Undefined')
    formulario_coment = forms.ComentarioForm(request.form)
    if request.method == 'POST' and formulario_coment.validate():
        usu= formulario_coment.usuario.data
        mail = formulario_coment.email.data
        coment = formulario_coment.comentario.data
        return 'usuario: {} , email {} , comentario {}'.format(usu , mail , coment)

    title = 'comentarios'
    return render_template('coment.html',title=title, form =formulario_coment )

@app.route('/ajax-login', methods = ['POST'] )
def ajax_login():
   
    username = request.form['username']
    password = request.form['password']
    # mi validacion
    response ={'status': 200, 'username': username,'password':password, 'id':1}
    return json.dumps( response)


if __name__ == '__main__':
    csrf.init_app(app)
    app.run(port= 8000)