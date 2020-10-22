from flask import Flask 

app = Flask(__name__) 
@app.route('/') 
def index():
    return 'hola mundo , que tal estas. Soy Pedro'

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
    app.run(debug= True,port= 8000)