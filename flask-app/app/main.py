from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return  "<h1>test</h1>" 

if __name__ == '__main__':

    app.run(host='0.0.0.0',debug =True , port=80)
