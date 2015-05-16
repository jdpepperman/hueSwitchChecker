import requests
import json
import time
import os

def setLightsToNormalScene():
    requests.put("http://192.168.1.124/api/joshuaserver/lights/1/state", data=json.dumps({"on":True, "sat":155, "bri":254, "hue":14704}))
    print(r.status_code, r.reason)
    requests.put("http://192.168.1.124/api/joshuaserver/lights/2/state", data=json.dumps({"on":True, "sat":220, "bri":254, "hue":34439}))
    print(r.status_code, r.reason)
    requests.put("http://192.168.1.124/api/joshuaserver/lights/3/state", data=json.dumps({"on":True, "sat":220, "bri":254, "hue":34439}))
    print(r.status_code, r.reason)

def setLightsToOff():
    requests.put("http://192.168.1.124/api/joshuaserver/lights/1/state", data=json.dumps({"on":False}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/2/state", data=json.dumps({"on":False}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/3/state", data=json.dumps({"on":False}))

r = requests.get("http://192.168.1.124/api/joshuaserver/lights/3")
parsed = json.loads(r.text)
previousState = bool(parsed['state']['reachable'])

setLightsToNormalScene()
#setLightsToOff()
#info = {"on":True}
#d = requests.put("http://192.168.1.124/api/joshuaserver/lights/1/state", data=json.dumps({"on" : True}))
#print(d.status_code, d.reason)
#print(d.content)
