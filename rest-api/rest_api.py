from flask import Flask
from flask_restful import Resource, Api
import requests
from firebase_data import FirebaseData

app = Flask(__name__)
api = Api(app)

fbo = FirebaseData()

class Containers(Resource):

    def get(self):

        all_containers = fbo.GetAllContainers()
        
        if all_containers != None:

            return {'message':"All containers available" , 'data':all_containers}

        else:

            return {'message': "Error"} , 404

api.add_resource(Containers,'/Containers')

if __name__ == '__main__':

    app.run(debug= True)