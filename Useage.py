# Import the modules
import requests
import json



class Useage:
    __init__():
    request =  requests.get("http://tackapi22.azurewebsites.net/api/useage")
    self.data = json.loads(request.text)

    def  current(self):
        if self.data != 0:
            return self.data["speed"] /float(10000
        else:
            return 0


    def volume(self):
        return self.data["usage"]
