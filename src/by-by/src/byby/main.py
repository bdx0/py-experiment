'''
Created on May 21, 2015

@author: dbd 
@version: 0.0.1
'''
import sys
from byby.core import get

def main(argv):
    print 'Hello ' + main.__name__ + ' !! '
    get.main()
    pass
       
if __name__ == '__main__':
    main(sys.argv)