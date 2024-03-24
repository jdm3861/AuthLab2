
import requests

auth_server = "http://127.0.0.1:5000/auth"
app_server = "http://127.0.0.1:5000/app"

def autheticate(username,password):


    credentials = {
        "username":username,
        "password": password
    }

    try:
        # request auth server 
        response = requests.post(auth_server,json=credentials)
        auth_response = response.json()
        print(auth_response)
        #check success 
        if auth_response["auth"] == "success":
            #send to app server 
            print(auth_response["token"])
            r = requests.post(app_server,json=auth_response)
            app_response = r.json()
            print(app_response)
        else:
            print("Auth Failed: invalid username or password")
    except Exception as e:
        print('Error: ' + str(e))

username = input("Enter your username: ")
password = input("Enter your password: ")

autheticate(username,password)
