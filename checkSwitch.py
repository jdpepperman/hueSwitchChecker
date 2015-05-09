#joshua pepperman

from phue import Bridge
import time

b = Bridge('192.168.1.124')

b.connect()

b.get_api()

def setLightsToNormalScene(self):
    b.set_light("Bedside", 'bri', 254)
    b.set_light("Desk", 'bri', 254)
    b.set_light("Corner", 'bri', 254)
    b.set_light("Bedside", 'sat', 155)
    b.set_light("Desk", 'sat', 220)
    b.set_light("Corner", 'sat', 220)
    b.set_light("Bedside", 'hue', 14704)
    b.set_light("Desk", 'hue', 34440)
    b.set_light("Corner", 'hue', 34440)

def setLightsToOff(self):
    b.set_light("Bedside", 'on', False)
    b.set_light("Desk", 'on', False)
    b.set_light("Corner", 'on', False)

previousState = b.get_light("Corner", 'reachable')

while True:
    currentState = b.get_light("Corner", 'reachable')
    #if it was on and now its off
    if previousState == True and currentState == False:
        #turn them all off
        setLightsToOff()
    #if it was off and now it is on
    elif previousState == False and currentState == True:
        #set them to the Normal scene
        setLightsToNormalScene()
    else:
        time.sleep(1)
    previousState = currentState
