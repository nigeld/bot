from flask import Flask
from flask import request
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object( DevelopmentConfig )

@app.route("/webhook", methods = ['GET'])
def webhook():
    verify_token = request.args.get('hub.verify_token', '')
    if verify_token == app.config['SECRET_KEY']:
        return request.args.get('hub.challenge', '')
    return 'Error al validar el secreto'

@app.route("/", methods = ['GET'])
def index():
    return 'Bienvenido a la pagina del bot'

if __name__ == '__main__':
    app.run(port = 8000)
