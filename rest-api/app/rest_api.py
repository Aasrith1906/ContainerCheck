from flask import Flask, url_for
from flask_restful import Resource, Api, reqparse , request
import requests
from firebase_data import FirebaseData
import datetime
import markdown

app = Flask(__name__)
api = Api(app)

fbo = FirebaseData()

@app.route('/',methods=['GET'])
def index():
    try:

        with open("Readme.md" , 'r') as readme_file:
            
            all_lines = readme_file.read()
            readme_file.close()
        
        html_ret = markdown.markdown(all_lines)

    except Exception as e:

        return {"message":str(e)} , 500
    
    return html_ret , 200

@app.route('/test',methods=['GET'])
def test():
    r = requests.get('127.0.0.1:5000/Containers')
    data = r.json()
    return data

class Containers(Resource):

    def get(self):

        try:

            all_containers = fbo.GetAllContainers()
        
        except Exception as e:

            return {"message":str(e)} , 500
        
        if all_containers != None:
            return {'message':"All containers available" , 'data':all_containers},200
        else:
            return {'message': "Error"} , 404

class IndividualContainer(Resource):
    
    def get(self,containername):

            try:

                container = fbo.GetSpecificContainer(containername)
            
            except Exception as e:

                return {"message":str(e)},500

            if container:
                return {'message':"Container found",'data':container}
            else:
                return {'message':"container not found"}, 404
        
    def post(self,containername):

        try:

            new_container = request.get_json()
            check_container = fbo.GetSpecificContainer(containername)

            required_keys = ["location","item","refill","last_date"]

            print(list(new_container.keys()))
            
            for key in required_keys:

                if key not in list(new_container.keys()):

                    return {"message":"invalid parameters"},500
            
            if check_container is not None:
                fbo.UpdateContainer(containername, new_container)
            else:
                fbo.SetContainer(containername,new_container)

            container_return = fbo.GetSpecificContainer(containername)
        
        except Exception as e:

            return {"message":str(e)} , 500

        if containername:
            return {'message':'container created','data':container_return} , 201
        else:
            return {'message':'container not created'} , 500

    def delete(self,containername):

        try:

            fbo.DeleteContainer(containername)

        except Exception as e:

            return {"message": str(e)},500
            
        return {'message':'container deleted','data':containername},202

class UserLoginResource(Resource):

    def post(self):

        pass

api.add_resource(Containers,'/Containers')
api.add_resource(IndividualContainer,'/Containers/<string:containername>')
api.add_resource(UserLoginResource, '/Login')

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=80)