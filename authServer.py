from flask import Flask, request, jsonify 
import requests, hashlib

app = Flask(__name__)
provider_url = "http://127.0.0.1/token.php"
secret_key = 123456789

@app.route('/auth',  methods=['POST'])
def authenticate_user():
    #make sure data is json
    content_type = request.headers.get('Content-Type')
    if(content_type != 'application/json'):
        return "Invalid content type"
    
    credentials = request.json

    #send the credentials to the provider
    try:
        response = requests.post(provider_url,json=credentials)
        provider_response = response.json()

        #check for success or failure
        provider_token = provider_response['access_token']
        if(provider_token):
            token = provider_token ^ secret_key #xor with secret key
            auth = 'success'
        else:
            token = ""
            auth = "fail"

        #return token to client
        oauth_token = {
            "auth": auth,
            "token": token
        }

        return jsonify(oauth_token)

    except Exception as e:
        print(e)

