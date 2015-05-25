import requests
import json
import time
import os
import sys

def setLightsToNormalScene():
    print("Turning lights on.")
    requests.put("http://192.168.1.124/api/joshuaserver/lights/1/state", data=json.dumps({"on":True, "sat":155, "bri":254, "hue":14704}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/2/state", data=json.dumps({"on":True, "sat":220, "bri":254, "hue":34439}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/3/state", data=json.dumps({"on":True, "sat":220, "bri":254, "hue":34439}))

def setAllLights(sat, bri, hue):
    requests.put("http://192.168.1.124/api/joshuaserver/lights/1/state", data=json.dumps({"sat":sat, "bri":bri, "hue":hue}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/2/state", data=json.dumps({"sat":sat, "bri":bri, "hue":hue}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/3/state", data=json.dumps({"sat":sat, "bri":bri, "hue":hue}))

#print(sys.argv)

if len(sys.argv) == 1:
    setLightsToNormalScene()
elif sys.argv[1] == 'red':
    setAllLights(254, 254, 0)
elif sys.argv[1] == 'orange': 
    setAllLights(254, 254, 6640)
elif sys.argv[1] == 'yellow': 
    setAllLights(254, 254, 17259)
elif sys.argv[1] == 'green': 
    setAllLights(254, 254, 25500)
elif sys.argv[1] == 'blue': 
    setAllLights(254, 254, 46920)
elif sys.argv[1] == 'indigo': 
    setAllLights(254, 254, 50704)
elif sys.argv[1] == 'violet': 
    setAllLights(254, 254, 56100)
