#! /usr/bin/env python

import drivers
from time import sleep
from datetime import datetime
from datetime import date
from subprocess import check_output
display = drivers.Lcd()
#IP = check_output(["hostname", "-I"], encoding="utf8").split()[0]

def currentTime():
    dateraw=datetime.now()
    timeFormat=dateraw.strftime("%-I:%M %p")
    return timeFormat
    
try:
    print("Writing to display")
    while True:
        def long_string(display, text='', num_line=1, num_cols=16):
            """ 
            Parameters: (driver, string to print, number of line to print, number of columns of your display)
            Return: This function send to display your scrolling string.
            """
            if len(text) > num_cols:
                display.lcd_display_string(text[:num_cols], num_line)
                sleep(1)
                for i in range(len(text) - num_cols + 1):
                    text_to_print = text[i:i+num_cols]
                    display.lcd_display_string(text_to_print, num_line)
                    sleep(0.2)
                sleep(1)
            else:
                display.lcd_display_string(text, num_line)
            
        avail = int(input("Enter a Value: "))
        cT=currentTime()
        today = str(date.today())
        me = "In a Meeting"
        av = "Available"
        pi = "Making Pi"
        
        #If 1, then status is available
        if (avail == 1):
            display.lcd_clear()
            display.lcd_backlight(1)
            display.lcd_display_string(av,1)
            display.lcd_display_string("as of "+cT, 2)
        #if 2, status is In a Meeting
        elif (avail == 2):
            display.lcd_clear()
            display.lcd_backlight(1)
            display.lcd_display_string(me, 1)
            display.lcd_display_string("as of "+cT, 2)
        #if 3, status is Making Pi
        elif (avail == 3):
            display.lcd_clear()
            display.lcd_backlight(1)
            display.lcd_display_string(pi, 1)
            display.lcd_display_string("as of "+cT, 2)
        #shut off backlight and just hsow time
        elif (avail == 504):
            display.lcd_clear()
            display.lcd_backlight(1)
            display.lcd_display_string("May the Force", 1)
            display.lcd_display_string("be with You!!", 2)
            
        elif (avail == 314):
            display.lcd_clear()
            display.lcd_backlight(1)
            display.lcd_display_string("I Like PI!!!!", 1)
            display.lcd_display_string("as of "+cT, 2)
        else:
            display.lcd_clear()
            display.lcd_backlight(0)
            display.lcd_display_string(today, 1)
            display.lcd_display_string(cT, 2)
        
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
    display.lcd_backlight(0)
    display.lcd_display_string(today, 1)
    display.lcd_display_string(cT, 2)
    
