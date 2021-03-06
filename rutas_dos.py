from flask import Flask 
#importamos la libreria request
from flask import request

app = Flask(__name__) 
@app.route('/') 
def index():
    return 'hola mundo '

# podemos recibir parametros
''' 
 si sabemos los parametros que vamos a recibir ,
 ejemplo - un nombre
'''
@app.route('/params/')
@app.route('/params/<name>') 
# todo lo que venga detras del / lo almacena como name
@app.route('/params/<name>/<int:num>') 
# todo lo que venga detras del / lo almacena como name y el siguiente / pedimos un numero entero
'''
http://127.0.0.1:9000/params/juan/25
si no es un numero entero , la pagina da error , si no va el segundo parametro , muestra el mensaje

´´´´
def params(name = 'valor por defecto', num ='ningun numero'):
     return 'el parametro es {} {}'.format(name,num)


#instruccion basica de python
if __name__ == '__main__':
    app.run(debug= True,port= 9000)