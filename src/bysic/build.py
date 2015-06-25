import os
import sys
import subprocess as sp

local_path = os.path.abspath(os.path.split(__file__)[0])
os.chdir(local_path)

def main():
  cmd = ['python ', 'setup.py', 'py2exe']
  p = sp.Popen(cmd, stderr=sp.PIPE, stdout=sp.PIPE)
  print p.communicate()[0]

if __name__ == "__main__":
  main()
