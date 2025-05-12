#a. import Flask
from flask import Flask, jsonify
#b. create object app
app = Flask(__name__)
#c. create route, method
@app.route('/halo', methods=['GET'])
#d. create fungction with return as response
def halo():
    return jsonify({"message": "Belajar Flask"})
#e. runc object default/host,port
if __name__ == '__main__':
    app.run(debug=True)
#Jika dengan docker : app.run(host='0.0.0.0', port=5000, debug=True)