# Import the modules
import requests
import json



class Useage:
    __init__():
    request =  requests.get("http://tackapi22.azurewebsites.net/api/useage")
    self.data = json.loads(request.text)

    def  current(self):
        return self.data["speed"]

    def volume(self):
        return self.data["usage"]
