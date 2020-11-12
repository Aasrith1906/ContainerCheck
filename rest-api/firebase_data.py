import pyrebase
import sys

class FirebaseData():

    def __init__(self):

        self.config = {
        "apiKey": "AIzaSyCwvOlRVZz5AKZUtpUrw9i0YBV3gjGVr-U",
        "authDomain": "container-management-295306.firebaseapp.com",
        "databaseURL": "https://container-management-295306.firebaseio.com/",
        "storageBucket": "container-management-295306.appspot.com",
        "serviceAccount": "ServiceAccount.json"
        }

        result  = self.init_app()
        
        if result == 0:
            print("Failed to init firebase !!!")
            sys.exit(0)

    def init_app(self):

        try:

            self.firebase = pyrebase.initialize_app(self.config)
            self.db = self.firebase.database()

        except Exception as e:

            print(str(e))
            
            return 0

    def PushData(self , child:str,data:dict): #pushes data to db 

        result = self.db.child(child).push(data)

        return result 

    def SetContainer(self , ContainerName:str, data:dict): #creates new container

        result = self.db.child("Containers").child(ContainerName).set(data)

        return result

    def UpdateContainer(self , ContainerName:str , data:dict): #updates container data

        result = self.db.child("Containers").child(ContainerName).update(data)
        return result 

    def GetAllContainers(self):

        all_containers = self.db.child("Containers").get()

        dict_containers = {}

        for container in all_containers.each():

            dict_containers[container.key()] = container.val()

        print(dict_containers)

        return dict_containers

    def GetSpecificContainer(self , container_name:str):
        
        all_containers = self.db.child("Containers").get()
        
        for container in all_containers.each():
            if container.key() == container_name:
                return container.val()

    def DeleteContainer(self, container_name:str):

        result = self.db.child("Containers").child(container_name).remove()
        return result

class StreamingFirebase(FirebaseData):

    pass
            
if __name__ == '__main__':

    obj = FirebaseData()
    obj.GetAllContainers()