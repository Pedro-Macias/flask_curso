from flask import Flask 
#importamos la libreria request
from flask import request

app = Flask(__name__) 
@app.route('/') 
def index():
    return 'hola mundo '
#podemos crear mas rutas ,  nunca se puede repetir el mismo metodo
@app.route('/saluda') 
def saluda():
    return 'Un saludo a todos '
# podemos recibir parametros
@app.route('/params') 
def params():
    '''
    si no recibe el parametro params1 , se ejecuta lo siguiente
    si recibe un parametro , ejemplo
    http://127.0.0.1:9000/params?params1=Pedro_Macias 
    imprime el parametro
    http://127.0.0.1:9000/params
    si no contiene ningun parametro , manda la informacion del string 
    '''
    param = request.args.get('params1', ' no contiene este parametro')
    '''
    podemos poner mas parametros ,
    http://127.0.0.1:9000/params?params1=Pedro_Macias&params2=%20Soy%20yo
    '''
    param_dos = request.args.get('params2', ' no contiene el segundo parametro')
    return 'el primer parametro es {} y el segundo {} '.format(param,param_dos)

# podemos cambiar el puerto al que nosotros necesitemos
'''
app.run(port= 8000)
''' 
#tambien le podemos colocar una bandera 
'''
si a la bandera 'debug= true , cuando cambiemos algo
al actualizar sale en la pantalla
si ponemos true , tendremos que reinciar la funcion

'''
#instruccion basica de python
if __name__ == '__main__':
    app.run(debug= True,port= 9000)