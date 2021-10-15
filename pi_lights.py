import socket
from neopixel import *
import time
from ast import literal_eval

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define important things for the lights to work
#just leave these as defualt and they should work
LED_COUNT = 30
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 225
LED_INVERT = False
LED_CHANNEL = 0

#which port should be used
port = 6969

#listen on specified port
print("Listening on port: ", port)
sock.bind(('',port))
sock.listen(5)

#loops forever until the stop command is recieved
while True:
    c, addr = sock.accept()
    print("Recieved connection")

    sequence = c.recv(1024).decode()

    #if it is array with custom sequence convert to list
    if sequence[0]=="[":
        sequence = literal_eval(sequence)
        custom_flag = True
        print(sequence[0]["blue"])

    #run the sequence
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    #hardocded sequences for testing
    if sequence=="Red":
        #turns all the lights red
        print("red sequence")
        for i in range(30):
            strip.setPixelColor(i,Color(0,255,0))
            strip.show()
    elif sequence=="Green":
        #turns all the lights green
        print("Green")
        for i in range(30):
            strip.setPixelColor(i,Color(255,0,0))
            strip.show()
    elif sequence=="Blue":
        #turns all the lights blue
        print("Blue")
        for i in range(30):
            strip.setPixelColor(i,Color(0,0,255))
            strip.show()
    elif sequence=="Clear":
        #turns of all lights
        print("Clear lights")
        for i in range(30):
            strip.setPixelColor(i,Color(0,0,0))
            strip.show()
    elif sequence=="Close":
        #stop the program
        c.close()
        break
    elif custom_flag==True:
        #for custom sequences
        print("Running custom sequence")
        for command in sequence:
            print(command)
            for i in range(int(command["light_start"]), int(command["light_end"])):
                strip.setPixelColor(i,Color(int(command["green"]),int(command["red"]),int(command["blue"])))
            strip.show()
            time.sleep(int(command["sleep"]))
    else:
        #if the sequcne is not known
        print("Unkown sequence")

        c.close()

print("Closing")
