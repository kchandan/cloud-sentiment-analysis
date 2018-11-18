# -*- coding: utf-8 -*-
import requests
from os.path import expanduser
import os
import configparser
import json

class aws:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(expanduser("~"),".azure/credentials"))
        region = config.get('default','region')
        key1 = config.get('default','key1')
        key2 = config.get('default','key2')
        self.azure_endpoint = "https://{}.api.cognitive.microsoft.com/text/analytics/v2.0/languages".format(region)
        self.key1 = key1
        self.key2 = key2
    def detect_language(self,text):
        headers = {
        'Content-Type': "application/json",
        'Ocp-Apim-Subscription-Key': self.key1,
        'Cache-Control': "no-cache"
        }
        payload = text
        print(self.azure_endpoint)
        print(self.key1)
        print(payload)
        print(headers)
        response = requests.request("POST", self.azure_endpoint, data=payload, headers=headers)
        print (response)
        if response.status_code != 200:
            return (False,response.status_code)
        print (response.text)
        return (True,response.text)


if __name__ == '__main__':

    a = aws()
    input_text = open("a.text").read()
    j = json.loads(input_text)
    status,text = a.detect_language(json.dumps(j))
    if status == True:
        j =json.loads(text)
        for doc in j['documents']:
            for lang in doc['detectedLanguages']:
                print(lang['name'],lang['iso6391Name'])



        
        




        