#!/usr/bin/python
# -*- coding: utf-8 -*-
  
from Quartz.CoreGraphics import *
from time import sleep
from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
import thread

flag = False

# Keyboard Events
class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)
        
# Where the magic begins
def handler(event):
    global flag
    try:
        #NSLog(u"%@", event)
        #print 'keycode: ' + str(event.keyCode())
        if (int(event.keyCode()) == 6): # 6 - Z Key
            flag = not(flag)
            status = 'activated' if flag else 'deactivated'
            print 'clicker ' + status
            clicker()
        elif (int(event.keyCode()) == 53): # 53 - ESC Key 
            AppHelper.stopEventLoop()
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()
    
# Mouse Events
def mouseEvent(type, posx, posy):  
    theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)
    result = CGEventPost(kCGHIDEventTap, theEvent)
    return result
    
def mouseclick(posx,posy):  
    up = mouseEvent(kCGEventLeftMouseDown, posx,posy)  
    down = mouseEvent(kCGEventLeftMouseUp, posx,posy)
    return str(up) + ' ' + str(down)

# the clicker
def clicker():
    global flag
    print 'clicker started'
    while(True):
        if(flag):
            ourEvent = CGEventCreate(None)
            currentpos = CGEventGetLocation(ourEvent) # Save current mouse position
            mouseclick(int(currentpos.x),int(currentpos.y))
            sleep(0.01);
    
#main function
def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
    
if __name__ == '__main__':
    thread.start_new_thread(clicker,())
    main()