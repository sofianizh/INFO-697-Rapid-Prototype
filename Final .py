# Write your code here :-)
from microbit import *

#sense the light
while True:
    if button_a.was_pressed(): Light Sensor
        Lightvalue = pin0.read_analog()
        if Lightvalue > 400:
            display.show(Image.HEART) #test
            sleep(100)
            pin1.write_digital(1) #Flash LED
            sleep(100)
        else:
            display.show(Image.SAD) #test
            pin1.write_digital(0) #Turn off the LED
            sleep(100）
    #the remainning part will be similar code of ultrasonic sensor
    
    #else: #Ultrasonic
        #if button_b.was_pressed():
