from flask import Flask, request

app = Flask(__name__)

secret_key = 123456789

@app.route('/app', methods = ['POST'])
def app():
    #make sure data is json
    content_type = request.headers.get('Content-Type')
    if(content_type != 'application/json'):
        return "Invalid content type"
    
    encrypt_token = request.json
    decrypt_token = encrypt_token ^ secret_key

    if decrypt_token['token'] == "":
        return "access denied"
    else:
        return "access granted"
