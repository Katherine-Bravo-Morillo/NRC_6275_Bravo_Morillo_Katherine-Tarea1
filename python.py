#importamos la libreria Flask
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

#---------------------------------------
#Ruta de pagina principal
#---------------------------------------
@app.route('/')

#Funcion para llamar al archivo de index
def index():
    return render_template('index.html')

#iniciamos la aplicacion
if __name__ == '__main__':
    app.run(debug=True)