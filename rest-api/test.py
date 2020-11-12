import unittest
import requests
from firebase_data import FirebaseData
from rest_api import app 


fbo = FirebaseData()

class FirebaseTests(unittest.TestCase):

    pass

class ApiTests(unittest.TestCase):

    def test_get_all_containers(self):

        r = requests.get("http://127.0.0.1:5000/Containers")
        all_containers = fbo.GetAllContainers()
        dict_data = r.json()
        print(all_containers)
        self.assertEqual(all_containers,dict_data["data"])


if __name__ == '__main__':

    unittest.main()