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

 #conexion base de datos almacenamiento de la tabla contact
 cur=mysql.connection.cursor()
 cur.execute('SELECT*FROM contacts')
 data=cur.fetchall()

 return render_template('index.html', contacts=data)

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

@app.route('/edit/<id>')
def edit_contact(id):

 cur = mysql.connection.cursor()
 #colcoamos el ide obtenido de la plantilla en la consulta sql
 cur.execute('SELECT*FROM contacts WHERE id=%s', (id))
 data=cur.fetchall()
 #indice 0 del array
 return render_template('edit-contact.html', contact=data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):

 if request.method=='POST':
  fullname=request.form['fullname']
  phone=request.form['phone']
  email=request.form['email']

  cur=mysql.connection.cursor()
  cur.execute("""
  UPDATE contacts
  SET  fullname=%s,
        email=%s,
        phone=%s
  WHERE id = %s    
  """, (fullname, phone, email, id))
  mysql.connection.commit()

  flash('Contact Updated Succesfuly')
  return redirect(url_for('Index'))


##ruta para borrar
@app.route('/delete/<string:id>')
def delete_contact(id):

 cur=mysql.connection.cursor()
 cur.execute('DELETE FROM contacts WHERE id = {0}'. format(id))
 mysql.connection.commit()
 flash('Contact Removed Successfully')

 return redirect(url_for('Index'))

if __name__ == '__main__':
##uso debug para que cada vez que se haga cambio el servidor renicie
 app.run(port=3000, debug=True)