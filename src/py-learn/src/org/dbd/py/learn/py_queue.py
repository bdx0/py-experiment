'''
Created on May 22, 2015

@author: CPU10157-local
'''
import Queue
from threading import Thread

def do_work(something):
    pass
def source():
    pass

def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

num_worker_threads = 10
q = Queue()
for i in range(num_worker_threads):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

for item in source():
    q.put(item)

q.join()  # block until all tasks are done

