from flask import Flask
from flask_restful import Resource, Api
import requests
from .firebase_data import FirebaseData

app = Flask(__name__)
api = Api(app)

