#importacion flask servidor y el render para las plantillas html
#request para solicitar
#redirect para deireccionar y url_for para asignar
#flash para mensajes entre vistas
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'vmedina'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'flaskcontacts'

mysql = MySQL(app)

#settings sessions
app.secret_key='mysecretkey'


#ruta principal
@app.route('/')
def Index():
 return render_template('index.html')

#ruta add contacto
@app.route('/add_contact', methods=['POST'])
def add_contact():
    #captura de datos
 if request.method == 'POST':
  fullname=request.form['fullname']
  phone=request.form['phone']
  email=request.form['email']

  #conexion sql insertar dato
  cur=mysql.connection.cursor()
  cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
  mysql.connection.commit()
  #mensaje
  flash('Contacto added successflully')
  ##redirecciona al index
  return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
 return 'edit contact'

@app.route('/delete')
def delete_contact():
 return 'delete'

if __name__ == '__main__':
##uso debug para que cada vez que se haga cambio el servidor renicie
 app.run(port=3000, debug=True)