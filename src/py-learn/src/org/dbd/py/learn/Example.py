'''
Created on May 21, 2015

@author: CPU10157-local
'''
import sys


def main(argv):
    print "Hello python: " + str(argv)
    ex = argv[1:]
    print ex
    ex.sort()
    print 'sort parameter' , ex
    ex = range(10)
    print ex
    ex.sort()
    print 'sort parameter' , ex
    a = [5, 2, 3, 1, 4]
    print a.sort()
    
if __name__ == '__main__':
    main(sys.argv);
