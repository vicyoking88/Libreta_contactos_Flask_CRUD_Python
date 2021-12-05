#importacion flask servidor y el render para las plantillas html
#request para solicitar
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'vmedina'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_HOST'] = 'flaskcontacts'

mysql = MySQL(app)

#ruta principal
@app.route('/')
def Index():
 return render_template('index.html')

#ruta add contacto
@app.route('/add_contact', methods=['POST'])
def add_contact():
 if request.method == 'POST':
  fullname=request.form['fullname']
  phone=request.form['phone']
  email=request.form['email']
  print(fullname)
  print(phone)
  print(email)
  return 'received'

@app.route('/edit')
def edit_contact():
 return 'edit contact'

@app.route('/delete')
def delete_contact():
 return 'delete'

if __name__ == '__main__':
##uso debug para que cada vez que se haga cambio el servidor renicie
 app.run(port=3000, debug=True)