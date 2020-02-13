from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    remote_ip = get_remote_ip()
    print(f'request:{request.environ}')
    return remote_ip

def get_remote_ip():
    # check client ip address (remote ip)
    # HTTP_X_REAL_IP >>> HTTP_X_FORWARDED_FOR (while proxy exist) >>> request.remote_addr (may show internal ip, e.g. 127.0.0.1)
    if 'HTTP_X_REAL_IP' in request.environ and request.environ['HTTP_X_REAL_IP']:
        remote_ip_address = request.environ['HTTP_X_REAL_IP']
    elif 'HTTP_X_FORWARDED_FOR' in request.environ and request.environ['HTTP_X_FORWARDED_FOR']:
        remote_ip_address = request.environ['HTTP_X_FORWARDED_FOR']
    else:
        remote_ip_address = request.remote_addr
    return remote_ip_address

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)