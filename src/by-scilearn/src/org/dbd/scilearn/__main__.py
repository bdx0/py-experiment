''' main.py ---
@author: duydb
@version: 0.0.1
'''

'''
Commentary:

'''

''' Code: '''

import sys
import os

script_directory_path = os.path.dirname(sys.argv[0])

def main(argv):
    print script_directory_path

if __name__ == '__main__':
    main(sys.argv)
