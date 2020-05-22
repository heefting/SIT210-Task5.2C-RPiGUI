from Tkinter import *
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Setup Leds
led0=LED(18)
led1=LED(23)
led2=LED(24)

leds = [led0,led1,led2]

# GUI setup
win = Tk()
win.title("LED Toggler")

# Led Commands
def test_function():
    print "Tested successfully"

def close():
    # Untoggle all leds
    for led_f in leds:
        led_f.off()
    RPi.GPIO.cleanup()
    win.destroy()

v = IntVar()

def show_choice():
    print v.get()

def ledToggle():
    # Untoggle all leds
    for led_f in leds:
        led_f.off()
    # Toggle chosen led
    led_ = leds[v.get()]
    if led_.is_lit:
        print "Already on"
    else:
        led_.on()

# Led Radio buttons
ledButton = Radiobutton(win, text='Blue', variable=v, value = 0, command=ledToggle, bg='bisque2', height=1, width=24)
ledButton.grid(row=0,column=1)

ledButton = Radiobutton(win, text='Green', variable=v, value = 1, command=ledToggle, bg='bisque2', height=1, width=24)
ledButton.grid(row=1,column=1)

ledButton = Radiobutton(win, text='Red', variable=v, value = 2, command=ledToggle, bg='bisque2', height=1, width=24)
ledButton.grid(row=2,column=1)

# Exit Button
exitButton = Button(win, text='Exit', command=close, bg='red', height=1, width=6)
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()





