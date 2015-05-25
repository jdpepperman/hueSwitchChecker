import requests
import json
import time
import os
def setAllLights(sat, bri, hue):
    requests.put("http://192.168.1.124/api/joshuaserver/lights/1/state", data=json.dumps({"sat":sat, "bri":bri, "hue":hue}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/2/state", data=json.dumps({"sat":sat, "bri":bri, "hue":hue}))
    requests.put("http://192.168.1.124/api/joshuaserver/lights/3/state", data=json.dumps({"sat":sat, "bri":bri, "hue":hue}))

def loopHardCode():
    sleepTime = .3
    while True:
        #red
        setAllLights(254, 254, 0)
        time.sleep(sleepTime)
        #orange
        setAllLights(254, 254, 6640)
        time.sleep(sleepTime)
        #yellow 
        setAllLights(254, 254, 17259)
        time.sleep(sleepTime)
        #green
        setAllLights(254, 254, 25500)
        time.sleep(sleepTime)
        #blue
        setAllLights(254, 254, 46920)
        time.sleep(sleepTime)
        #indigo
        setAllLights(254, 254, 50704)
        time.sleep(sleepTime)
        #violet
        setAllLights(254, 254, 56100)
        time.sleep(sleepTime)

def loopAllColors():
    sleepTime = .1
    while True:
        #100 is a good speed
        for i in range(0, 65535, 100):
            setAllLights(254, 254, i)

loopAllColors()
