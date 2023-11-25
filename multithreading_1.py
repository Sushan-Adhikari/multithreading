#Threads are like lightweight processes
#similar like processes but they use lot less resource
#Threads are like light-weight processes
#multiple threads in the same process share the same memory space so they can communicate with each other better and exchange data

#we need a threading module
import threading

#define two function for threading
#they can be made to run in parallel by using threading

import time

def function1():
    for x in range (10):
        time.sleep(1)
        print("one")

def function2():
    for x in range(10):
        time.sleep(1)
        print("two")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t1.start()
t2.start()
 

#suppose we have another code which we want to run only after the threads have completed
t1.join()
t2.join()
print("Printed after the thread completion")