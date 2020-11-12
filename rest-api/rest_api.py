from flask import Flask
from flask_restful import Resource, Api, reqparse , request
import requests
from firebase_data import FirebaseData
import datetime


app = Flask(__name__)
api = Api(app)

fbo = FirebaseData()



class Containers(Resource):

    def get(self):

        all_containers = fbo.GetAllContainers()
        
        if all_containers != None:
            return {'message':"All containers available" , 'data':all_containers},200
        else:
            return {'message': "Error"} , 404

class IndividualContainer(Resource):
    
    def get(self,containername):

            container = fbo.GetSpecificContainer(containername)

            if container:
                return {'message':"Container found",'data':container}
            else:
                return {'message':"container not found"}, 404
        
    def post(self,containername):

        new_container = request.get_json()
        check_container = fbo.GetSpecificContainer(containername)

        if check_container is not None:
            fbo.UpdateContainer(containername, new_container)
        else:
            fbo.SetContainer(containername,new_container)

        container_return = fbo.GetSpecificContainer(containername)
        if containername:
            return {'message':'container created','data':container_return} , 201
        else:
            return {'message':'container not created'} , 500

api.add_resource(Containers,'/Containers')
api.add_resource(IndividualContainer,'/Containers/<string:containername>')

if __name__ == '__main__':

    app.run(debug= True)