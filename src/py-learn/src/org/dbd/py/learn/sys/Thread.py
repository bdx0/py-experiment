'''
Created on May 22, 2015

@author: CPU10157-local
'''

'''
http://pymotw.com/2/threading/index.html
http://www.python-course.eu/threads.php
http://pymotw.com/2/threading/
http://www.tutorialspoint.com/python/python_multithreading.htm
http://en.wikibooks.org/wiki/Python_Programming/Threading
http://stackoverflow.com/questions/2905965/creating-threads-in-python
'''
import thread
import time

# Define a function for the thread
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))

# Create two threads as follows
try:
    thread.start_new_thread(print_time, ("Thread-1", 2,))
    thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print "Error: unable to start thread"

while 1:
    pass
