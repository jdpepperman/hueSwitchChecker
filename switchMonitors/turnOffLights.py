import requests
import json
import time
import os

def setLightsToOff():
    print("Turning lights off.")
    requests.put("http://192.168.1.124/api/joshuaserver/lights/1/state", data=json.dumps({"on":False}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/2/state", data=json.dumps({"on":False}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/3/state", data=json.dumps({"on":False}))

r = requests.get("http://192.168.1.124/api/joshuaserver/lights/3")
parsed = json.loads(r.text)
previousState = bool(parsed['state']['reachable'])

while previousState == True:
    d = requests.get("http://192.168.1.124/api/joshuaserver/lights/3")
    parsed = json.loads(d.text)
    currentState = bool(parsed['state']['reachable'])

    if currentState == False:
        setLightsToOff()
        os.system("python /home/joshua/programming/lights/switchMonitors/turnOnLights.py")
    else:
        time.sleep(1)
    previousState = currentState
