# Import the modules
import requests
import json


class Useage:
    def __init__(self):
        request =  requests.get("http://tackapi22.azurewebsites.net/api/useage")
        self.data = json.loads(request.text)
        print(self.data)

    def  current(self):
        self.data["speed"]


    def volume(self):
        return self.data["usage"]
