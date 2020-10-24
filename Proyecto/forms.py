from flask_wtf import FlaskForm
from wtforms import Form 
from wtforms import StringField , TextField
from wtforms.fields.html5 import EmailField



class ComentarioForm(Form):
    usuario = StringField('Usuario')
    email = EmailField('Correo electronico')
    comentario = TextField('Comentario')

