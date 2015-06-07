import sys

python_bin = sys.executable

def main(argv):
 print argv

def test1():
 print test1.__name__

if __name__ == '__main__':
 main(sys.argv)

