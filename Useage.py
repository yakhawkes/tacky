# Import the modules
import requests
import json



class Useage:

    def  current(self):
        request =  requests.get("http://www.reddit.com/user/spilcm/about/.json")
        data = json.loads(request.text)
        return 0.25#(float(data['speed'])/100)*-1
