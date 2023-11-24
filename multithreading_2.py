#there is no actual multithreading in python because of global interpreter lock
#we have pseudo multithreading where we run things concurrently
#we are switching between the tasks and using the downtimes of the different task to execute the other task
#downtime: we send a request and wait for a response there is some downtime
#waiting for a user input also has some downtime

import threading
import time #for sleep function

# done = False

# def worker():
#     counter = 0
#     while not done:
#         time.sleep(1)
#         counter +=1
#         print(counter)
# #specifying a thread
# #we need the instance of the function in target= 
# #.start is used to start the thread right away

# threading.Thread(target=worker).start()
# #worker function will execute as a separate thread

# # worker() #no need to specify this after threading has started


# #suppose that I want to quit the loop by pressing enter while it is iterating
# #the program will not reach here as the loop continues endlessly

# input("Press enter to quit")
# done = True


#using daemon thread: if the main thread terminates the other thread specifies as 'daemon' also terminates

def worker(text):
    counter = 0
    while True:
        time.sleep(1)
        counter+=1
        print(f"{text}:{counter}")

#even though the loop is always valid, it stops when we press an enter 
#daemon ensures that the specified thread stops when the main thread stops
#if nothing else is running, quit it
t1 = threading.Thread(target=worker, daemon=False, args=("XYZ",))
t2 = threading.Thread(target=worker, daemon=True, args=("ABC",))

t1.start()
t2.start()

#to wait for the threads
t1.join()
t2.join()
  

#after the join the following line will not be executed until the threads are completed

input("press enter to quit")
done = True


