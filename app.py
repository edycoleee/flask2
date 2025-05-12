#a. import Flask
from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger

#b. create object app
app = Flask(__name__)

CORS(app)  # Aktifkan CORS untuk semua route
app.config['SWAGGER'] = {
    'title': 'COBA API',
    'uiversion': 3
}
swagger = Swagger(app)

#c. create route, method
# Register blueprint >> Seperti Router() di Express
from routes.belajar import belajar_bp  # perbaikan import

app.register_blueprint(belajar_bp)

#e. runc object default/host,port
if __name__ == '__main__':
    app.run(debug=True)
#Jika dengan docker : app.run(host='0.0.0.0', port=5000, debug=True)