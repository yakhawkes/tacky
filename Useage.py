# Import the modules
import requests
import json



class Useage:

    def  current(selfself):
        request =  requests.get("http://www.reddit.com/user/spilcm/about/.json")
        data = json.loads(r.text)
        return data['speed']