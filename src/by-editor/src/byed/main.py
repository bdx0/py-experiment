import sys

python_bin = sys.executable

def main(argv):
 filename = None
 if len(argv) > 1 :
  filename = argv[1]
 
 module_name = '%s' % filename if filename != None else 'ex1'
 editor = __import__('byed.' + module_name, globals(), locals(), [module_name], -1)
 editor.main(argv[2:])

if __name__ == '__main__':
 main(sys.argv)

