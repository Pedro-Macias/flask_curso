#todos los archivos HTML , tienen que estar en una carpeta llamada TEMPLATES




from flask import Flask 
#Necesitamos importar la libreria render_temlate

from flask import render_template
'''
 SI NO queremos utilizar la carpeta TEMPLATES que es la que esta por default
tendriamos que indicarselo a python
app = Flask(__name__, template_folder = 'nombre-carpeta')
'''
app = Flask(__name__) 
@app.route('/user/<name>')
def user(name='pedro'):
    age = 20
    my_list=[1,3,5,7, 'string',1.56]
    # ponemos el nombre del render que vamos a indexar
    return render_template('user.html',name=name, age=age, lista=my_list)

if __name__ == '__main__':
    app.run(debug= True,port= 8000)