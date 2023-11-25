#this is another method for synchronization
#Refer to the synchronization_locking for understanding about synchronization

#it does not lock the resource completely but limits the access to a resource to a maximum value

import threading
import time

semaphore = threading.BoundedSemaphore(value = 5)   #it allows for 5 threads to access a resource

#defining function for multiple threads
#using thread_number as the argument

def access(thread_number):
    print("{} is trying to access!".format(thread_number))
    #trying to acquire a semaphore
    #if we haven't had 5 accesses already, we will be given access
    semaphore.acquire()
    print("{} was granted access!".format(thread_number))
    time.sleep(10)
    #After 10 seconds
    #we are releasing the semaphore
    print("{} is now releasing!".format(thread_number))
    semaphore.release()

#loop for starting 10 threads with different thread numbers
for thread_number in range (1,11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)

