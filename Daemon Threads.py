#they are running in the background and the script terminates even though they are running
#they are not vital to the program
#for other threads, the program waits for all of them to terminate
# nobody waits for daemon threads
# we could use it for constantly reading something from a file, a web API, and as soon as everything else is done, the threads also terminate

#example to show a thread(daemon thread) reading from a text file and the other(ordinary) thread printing it

import threading
import time

path = "text.txt"
text = ""

def readFile(): #it reads the file endlessly
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)   #it takes three seconds to go again to the top and read the file
def printloop():
    for x in range(30): #it prints 30 times
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True) #after main thread terminates, it terminates automatically
t2 = threading.Thread(target=printloop) #this is the main thread

t1.start()
t2.start()

#For understanding, change the contents in the text.txt while the program is running
