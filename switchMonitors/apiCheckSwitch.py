import requests
import json
import time
import os

def setLightsToNormalScene():
    print("Turning lights on.")
    requests.put("http://192.168.1.124/api/joshuaserver/lights/1/state", data=json.dumps({"on":True, "sat":155, "bri":254, "hue":14704}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/2/state", data=json.dumps({"on":True, "sat":220, "bri":254, "hue":34439}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/3/state", data=json.dumps({"sat":220, "bri":254, "hue":34439}))
    lightsAreOn = True

def setLightsToOff():
    print("Turning lights off.")
    requests.put("http://192.168.1.124/api/joshuaserver/lights/1/state", data=json.dumps({"on":False}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/2/state", data=json.dumps({"on":False}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/3/state", data=json.dumps({"on":False}))
    lightsAreOn = False

lightsAreOn = True
r = requests.get("http://192.168.1.124/api/joshuaserver/lights/3")
parsed = json.loads(r.text)
previousCornerIsReachable = bool(parsed['state']['reachable'])

while True:
    cornerr = requests.get("http://192.168.1.124/api/joshuaserver/lights/3")
    deskr = requests.get("http://192.168.1.124/api/joshuaserver/lights/2")
    bedsider = requests.get("http://192.168.1.124/api/joshuaserver/lights/1")
    cornerparsed = json.loads(cornerr.text)
    deskparsed = json.loads(deskr.text)
    bedsideparsed = json.loads(bedsider.text)
    currentCornerIsReachable = bool(cornerparsed['state']['reachable'])
    currentDeskIsOn = bool(deskparsed['state']['on'])
    currentBedsideIsOn = bool(bedsideparsed['state']['on'])
    
    if previousCornerIsReachable == True and currentCornerIsReachable == False:
        setLightsToOff()
    elif previousCornerIsReachable == False and currentCornerIsReachable == True:

        setLightsToNormalScene()
    else:
        if previousCornerIsReachable == True:
            time.sleep(1)
        else: 
            time.sleep(.33)
    previousCornerIsReachable = currentCornerIsReachable

os.system("echo 'The process on the server that monitors the light in the bedroom that is powered by the lightswitch has ended.' | mail -s 'SERVER: apiCheckSwitch.py Ended' joshuapepperman@gmail.com")
