# synchronization deals with how to use multiple threads at once that tries to access the same resource
# For example: if there are 14 threads accessing the same resource via a RESTful API, or any same resource
# Suppose one thread is changing the data, other is reading it, other is trying to delete it, what happens then? 
# How to manage the threads? 
#This is where synchronization comes in

#first way to do this is by locking

#let's say we are using two threads: one tries to double the number and the other tries to divide the same number by 2 

import threading
import time


# x = 8192    #this is the shared resource

# def double():
#     global x    #I am accessing a global variable and I want to change it in this function
#     while x < 16384:
#         x *= 2
#         print(x)
#         time.sleep(1)
#     print("Reached the maximum")

# def half():
#     global x
#     while x>1:
#         x /=2
#         print(x)
#         time.sleep(1)


# t1 = threading.Thread(target=half)
# t2 = threading.Thread(target=double)

# t1.start()
# t2.start()


#this above code goes to an endless loop as both threads are executed simultaneously 
# one halves it while the other doubles it, the while loop is never false on both of the cases


#locking method locks the resource so that one thread can use it at a time and frees it at the end to be used by the other
# this is like serial execution

x = 8192    #this is the shared resource
lock = threading.Lock()

def double():
    global x, lock
    lock.acquire()  #lock the resources for this thread
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached the maximum!")
    lock.release()  #release the resources to be used by another

def half():
    global x, lock
    lock.acquire()
    while x>1:
        x /= 2 
        print(x)
        time.sleep(1)
    print("Reached the minimum!")
    lock.release() 

t1 = threading.Thread(target=half)
t2 = threading.Thread(target=double)

t1.start()
t2.start()

