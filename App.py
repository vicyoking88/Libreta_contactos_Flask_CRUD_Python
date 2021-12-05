from flask import Flask

app = Flask(__name__)

#ruta principal
@app.route('/')
def Index():
 return'Hello World'
#ruta add contacto
@app.route('/add_contact')
def add_contact():
 return'Ad Contact'

@app.route('/edit')
def edit_contact():
 return 'edit contact'

@app.route('/delete')
def delete_contact():
 return 'delete'

if __name__ == '__main__':
##uso debug para que cada vez que se haga cambio el servidor renicie
 app.run(port=3000, debug=True)