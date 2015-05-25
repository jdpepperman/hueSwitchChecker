import requests
import json
import time
import os

def setLightsToNormalScene():
    print("Turning lights on.")
    requests.put("http://192.168.1.124/api/joshuaserver/lights/1/state", data=json.dumps({"on":True, "sat":155, "bri":254, "hue":14704}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/2/state", data=json.dumps({"on":True, "sat":220, "bri":254, "hue":34439}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/3/state", data=json.dumps({"on":True, "sat":220, "bri":254, "hue":34439}))

r = requests.get("http://192.168.1.124/api/joshuaserver/lights/3")
parsed = json.loads(r.text)
previousState = bool(parsed['state']['reachable'])

while previousState == False:
    d = requests.get("http://192.168.1.124/api/joshuaserver/lights/3")
    parsed = json.loads(d.text)
    currentState = bool(parsed['state']['reachable'])
    
    if currentState == True:
        setLightsToNormalScene()
        os.system("python /home/joshua/programming/lights/switchMonitors/turnOffLights.py")
    else:
        time.sleep(.3)
    previousState = currentState
