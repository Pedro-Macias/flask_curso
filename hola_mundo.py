from flask import Flask 

app = Flask(__name__) # nuevo objeto , recibe como parametro __name__
# indicarle a que ruta tiene que acceder
 # wrap o un decorador
@app.route('/') # como parametro le ponemos la ruta , en este caso '/'
# una funcion 
def index():
    return 'hola mundo' # regresar un string


app.run() # ejecutar el servidor por default en el puerto 5000
