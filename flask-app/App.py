from flask import Flask
import requests

app = Flask(__name__)

 


@app.route('/',methods=['GET'])
def index():
    r = requests.get("http://192.168.1.56:31351/Containers")
    return  "<h1>oye shreeya you are cute</h1>"

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0',port=5002)