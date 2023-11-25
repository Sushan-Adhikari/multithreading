#Queues are data structures with FIFO
#when we have multiple threads running, we need to have a structured way for getting the data in and out
#why queues?
# let's say numbers=[1, 2, 3, 4, 5, 6, 7]
# we have three threads that takes and evaluates(anything, let's say square) 1st, 2nd, and 3rd numbers respectively
# after a thread is completed it has to check the next element which has not been processed 
# we need a way to note which numbers are processed by the threads
# we could use counter = how many elements have been processed
# if thread 1 sets the counter to 1, thread 2 to 2, and thread 3 to 3
# what if threads 1 and 2 finish processing at the same time
#the number would then increase from (3 say it was before) to 5(cuz thread 2 increases by 2)
#the number 4 would be skipped because of this
#need a structured way for processing data

#in a queue, we use FIFO, once an element is out and processed it would be removed from the queue

#creating a FIFO Queue
# import queue

# q = queue.Queue()

# numbers = [10, 20, 30, 40, 50, 60, 70]
# for number in numbers:
#     q.put(number)

# print(q.get())  #first element
# print(q.get())  #second element

#we can also create a Last In First Out Queue

# import queue

# q = queue.LifoQueue()

# numbers= [1,2,3,4,5,6,7]
# for x in numbers:
#     q.put(x)

# print(q.get()) #last element
# print(q.get())  #second to last element


#we can also create priority queue

import queue

q= queue.PriorityQueue()    #priority queue
#lower the number higher the priority

#we need to pass the priority and the data into the queue as a tuple

q.put((2, "Hello World!"))
q.put((10, 54))
q.put((5, 6.87))
q.put((1, True))

while not q.empty():
    # print(q.get())
    #to only get the data, print the data at index[1]
    print(q.get()[1])

#Its amazing application can be seen at port scanner
#we would check if any ports are open in a network for revealing the vulnerabilities of the network


