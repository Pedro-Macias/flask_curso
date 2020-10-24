from flask_wtf import FlaskForm
from wtforms import Form 
from wtforms import StringField , TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators


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

