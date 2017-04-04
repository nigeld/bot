from flask import Flask
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_objec( DevelopmentConfig )


@app.route("/", method = ['GET'])
def index():
    return 'Bienvenido a la pagina del bot'

if __name__ == '__main__':
    app.run(port = 8000)
