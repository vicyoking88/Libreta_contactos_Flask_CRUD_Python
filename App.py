from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
 return'Hello World'

if __name__ == '__main__':
##uso debug para que cada vez que se haga cambio el servidor renicie
 app.run(port=3000, debug=True)