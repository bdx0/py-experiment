# Time.py --- 
#
# http://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution
# http://www.huyng.com/posts/python-performance-analysis/
import time

def main():
    time.sleep(0.01)

start_time = time.clock()
main()
print time.clock() - start_time, "seconds"