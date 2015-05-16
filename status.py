import requests
import json

def printjson(jsonToPrint):
    parsed = json.loads(jsonToPrint)
    print(json.dumps(parsed, indent=4, sort_keys=True))

printjson(requests.get("http://192.168.1.124/api/joshuaserver/lights").text)
