#Events: things in python that we can trigger, we can react to them

import threading

event = threading.Event()   #event

#we can trigger and wait for this event
#it is an element, an object that has a function to be triggered

def myfunction():
    print("Waiting for event to trigger....\n")
    event.wait()
    print("performing action XYZ now...")

t1 = threading.Thread(target=myfunction)
t1.start()

x = input("Do you want to trigger the event? (y/n)")
if x == "y":
    event.set()



