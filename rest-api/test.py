import unittest
import requests
from firebase_data import FirebaseData
from rest_api import app 


fbo = FirebaseData()

class ApiTests(unittest.TestCase):

    def test_get_all_containers(self):

        r = requests.get("http://127.0.0.1:5000/Containers")
        all_containers = fbo.GetAllContainers()
        dict_data = r.json()
        self.assertEqual(all_containers,dict_data["data"])
    
    def test_get_single_container(self):

        r = requests.get("http://127.0.0.1:5000/Containers/container1")
        dict_data = r.json()
        container = fbo.GetSpecificContainer("container1")
        self.assertEqual(container,dict_data["data"])

    def test_post_new_container(self):
        
        test_data = {"location":"kitchen","item":"testitem","refill":"false","last_date":"12-11-2020"}
        requests.post("http://127.0.0.1:5000/Containers/testcontainer",json=test_data)
        get_container = fbo.GetSpecificContainer("testcontainer")
        self.assertEqual(get_container,test_data)

    def test_delete_new_container(self):

        requests.delete("http://127.0.0.1:5000/Containers/testcontainer")
        r = requests.get("http://127.0.0.1:5000/Containers/testcontainer")
        self.assertEqual(r.json()["message"] , "container not found")


if __name__ == '__main__':

    unittest.main()