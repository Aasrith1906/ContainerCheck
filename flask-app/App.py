from flask import Flask
import requests

app = Flask(__name__)

 
r = requests.get("http://127.0.0.1:57096/Containers")

@app.route('/',methods=['GET'])
def index():
   
    return r.json()

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0',port=5001)