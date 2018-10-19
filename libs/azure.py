import requests
from os.path import expanduser
import os
import configparser

class aws:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(expanduser("~"),".azure/credentials"))
        region = config.get('default','region')
        key1 = config.get('default','key1')
        key2 = config.get('default','key2')
        self.azure_endpoint = "https://{}.api.cognitive.microsoft.com/text/analytics/v2.0".format(region)
        self.key1 = key1
        self.key2 = key2
    def detect_language(self,lang,text):
        headers = {
        'Content-Type': "application/json",
        'Ocp-Apim-Subscription-Key': self.key1,
        'Cache-Control': "no-cache"
        }
        payload = text

        response = requests.request("POST", url, data=payload, headers=headers)
        if response.status_code != 200:
            return (False,response.status_code)
        return (True,response.text)
        
        




        