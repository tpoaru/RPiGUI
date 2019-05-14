from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

"Variables for LED pins"
green_led = LED(20)
red_led = LED(21)
blue_led = LED(16)
 

window = Tk()
window.title("RGB Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')

"function for the red LED to toggle on/off"
def redLedToggle():
    if red_led.is_lit:
        red_led.off()
        red_led_button["text"] = "Turn Red LED on"
    else:
        red_led.on()
        red_led_button["text"] = "Turn Red LED off"
        
"function for the green LED to toggle on/off"
def greenLedToggle():
    if green_led.is_lit:
        green_led.off()
        green_led_button["text"] = "Turn Green LED on"
    else:
        green_led.on()
        green_led_button["text"] = "Turn Green LED off"
        
"function for the blue LED to toggle on/off"
def blueLedToggle():
    if blue_led.is_lit:
        blue_led.off()
        blue_led_button["text"] = "Turn Blue LED on"
    else:
        blue_led.on()
        blue_led_button["text"] = "Turn Blue LED off"
        
def exitProgram():
    print("Exit Button Press")
    GPIO.cleanup()
    window.destroy()
    window.mainloop()
    

red_led_button = Button(window, text = 'Red LED', font = myFont, command = redLedToggle, bg = 'red', height = 8, width = 15)
green_led_button = Button(window, text = 'Green LED', font = myFont, command = greenLedToggle, bg = 'green', height = 8, width = 15)
blue_led_button = Button(window, text = 'Blue LED', font = myFont, command = blueLedToggle, bg = 'blue', height = 8, width = 15)
exitProgram = Button(window, text = 'Exit', font = myFont, command = exitProgram, bg = 'white', height = 8, width = 15)

red_led_button.grid(row = 0 , column = 1)
green_led_button.grid(row = 0 , column = 2)
blue_led_button.grid(row = 0 , column = 3)
exitProgram.grid(row = 2 , column = 2)

