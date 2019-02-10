from flask import Flask, jsonify, request, session
from flask_cors import CORS # Allow Cross domain AJAX, 2018-08-25

app = Flask(__name__)
CORS(app) # Fix Cross domain AJAX issue, 2018-08-25

@app.route('/')
def hello_world():
  #say = request.args.get('say',type = str)
  #return say
  return 'Hello, flask session!'

if __name__ == '__main__':
  #app.config['JSON_AS_ASCII'] = False # fix return 中文 json 亂碼問題
  app.debug = True

  app.run(host='0.0.0.0', port=8080)