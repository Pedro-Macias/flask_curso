from flask_wtf import FlaskForm
from wtforms import Form 
from wtforms import StringField , TextField
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField
from wtforms import HiddenField
from wtforms import validators

def lengh_campoVacio(form,field):
    if len(field.data)>0:
        raise validators.ValidationError('el campo debe de estar vacio')

class ComentarioForm(Form):
    usuario = StringField('Usuario',
               [ 
                   validators.Required(),
                   validators.length(min=3, max = 10, message='ingrese un usuario minimo 3 caracteres y maximo 10')
               ]
               )
    email = EmailField('Correo electronico',
                [
                validators.Required()
                
                ]
                )
    comentario = TextField('Comentario')
    # este campo siempre estara vacio
    campo_vacio = HiddenField('',[lengh_campoVacio])

class LoginForm(Form):
    username = StringField('Usuario',
               [ 
                   validators.length(min=5, max = 10, message='ingrese un usuario minimo 5 caracteres y maximo 10'),
                   validators.Required(message = 'el nombre de usuario es Obligatio')
                   
               ]
               )
    password = PasswordField('Contraseña',
                [
                validators.Required('la contraseña es Obligatoria')
                
                ]
                )
    

