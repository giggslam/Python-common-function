from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

WHITELIST_IP = ['101.78.238.73']

@app.before_request
def before_request():
    print('before_request() ...')

    print(f'request.endpoint:{request.endpoint}') #

    remote_ip = get_remote_ip()

    # only whitelist ip can access specific endpoint (route)
    RESTRICTED_ENDPOINT_FUNCTIONS = ['get_retricted_func'] # function name, not routing name

    if request.endpoint in RESTRICTED_ENDPOINT_FUNCTIONS:
        print('found retricted endpoint, checking remote ip now ...')
        if remote_ip not in WHITELIST_IP:
            print('remote ip not in whitelist, DENIED TO ACCESS!')
            return 'not allow to access'
    else:
        print('NOT RESTRICTED_ENDPOINT_FUNCTIONS')

    print('... before_request()')

@app.route("/", methods=["GET"])
def helloworld():
    return 'helloworld', 200

@app.route("/retricted_route", methods=["GET"])
def get_retricted_func():
    remote_ip = get_remote_ip()
    print(f'request:{request.environ}')
    return remote_ip

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    remote_ip = get_remote_ip()
    print(f'request:{request.environ}')
    return remote_ip

def get_remote_ip():
    # check client ip address (remote ip)
    # HTTP_X_REAL_IP >>> HTTP_X_FORWARDED_FOR (while proxy exist) >>> request.remote_addr (may show internal ip, e.g. 127.0.0.1)
    print(f'request.environ:{request.environ}') # DEBUG
    if 'HTTP_X_REAL_IP' in request.environ and request.environ['HTTP_X_REAL_IP']:
        remote_ip_address = request.environ['HTTP_X_REAL_IP']
    elif 'HTTP_X_FORWARDED_FOR' in request.environ and request.environ['HTTP_X_FORWARDED_FOR']:
        remote_ip_address = request.environ['HTTP_X_FORWARDED_FOR']
    else:
        remote_ip_address = request.remote_addr
    print(f'remote_ip_address:{remote_ip_address}')
    return remote_ip_address

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)