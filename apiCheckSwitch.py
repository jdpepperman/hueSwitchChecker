import requests
import json
import time
import os

def setLightsToNormalScene():
    print("Turning lights on.")
    requests.put("http://192.168.1.124/api/joshuaserver/lights/1/state", data=json.dumps({"on":True, "sat":155, "bri":254, "hue":14704}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/2/state", data=json.dumps({"on":True, "sat":220, "bri":254, "hue":34439}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/3/state", data=json.dumps({"on":True, "sat":220, "bri":254, "hue":34439}))

def setLightsToOff():
    print("Turning lights off.")
    requests.put("http://192.168.1.124/api/joshuaserver/lights/1/state", data=json.dumps({"on":False}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/2/state", data=json.dumps({"on":False}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/3/state", data=json.dumps({"on":False}))

r = requests.get("http://192.168.1.124/api/joshuaserver/lights/3")
parsed = json.loads(r.text)
previousState = bool(parsed['state']['reachable'])

while True:
    r = requests.get("http://192.168.1.124/api/joshuaserver/lights/3")
    parsed = json.loads(r.text)
    currentState = bool(parsed['state']['reachable'])
    
    print("\n")
    print("Prev state: " + str(previousState))
    print("Curr state: " + str(currentState))

    if previousState == True and currentState == False:
        setLightsToOff()
    elif previousState == False and currentState == True:
        setLightsToNormalScene()
    else:
        #time.sleep(5)
        pass
    previousState = currentState

os.system("echo 'The process on the server that monitors the light in the bedroom that is powered by the lightswitch has ended.' | mail -s 'SERVER: apiCheckSwitch.py Ended' joshuapepperman@gmail.com")
