#todos los archivos HTML , tienen que estar en una carpeta llamada TEMPLATES




from flask import Flask 
#Necesitamos importar la libreria render_temlate

from flask import render_template
app = Flask(__name__) 
@app.route('/') 
def index():
    name = 'Pedro'
    return render_template('index.html',name=name)
# creamos la ruta a otra pagina
@app.route('/cliente') 
def cliente():
    list_name = ['Luis','Juan','Pepe']
    return render_template('cliente.html',lista=list_name)    

if __name__ == '__main__':
    app.run(debug= True,port= 9000)