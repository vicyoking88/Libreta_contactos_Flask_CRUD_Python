from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
 return'Hello World'

@app.route('/add_contact')
def add_contact():
 return'Agregar contacto'

if __name__ == '__main__':
##uso debug para que cada vez que se haga cambio el servidor renicie
 app.run(port=3000, debug=True)