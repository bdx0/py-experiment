'''
The File Mechanics Module contains a set of methods that are used
when dealing with a file in python.

The modules class File() contains mthods on opening, closing,
renaming, creating, encrypting, decrypting and closing.

'''
import os
import shutil
import zlib
import base64

class File():
    ''' This class contains these Methods:
        |
        |-create()
        |   Creates a new file with the name givin in File(filename)
        |   and returns True if it were successful or the Exception if not.
        |
        |-delete()
        |   Deletes the file passed in File(filename) and returns True
        |   if successful and the Exception if not.
        |
        |-openFile(oldName)
        |   opens the file oldName and returns the contents of that file or False
        |   if unsuccessful. Also call File(oldName) to be able to use all these
        |   methods on the newly opened file.
        |
        |-rename(newName)
        |   Renames the file passed in File(filename) with newName and returns True if successfully
        |   renamed or the Exception if not.
        |
        |-encrypt()
        |   Encrypts and compresses the file passed in File(filename) with th zlib and base64 modules at
        |   level 9 compression. This method returns True if successful and the Exception if not.
        |
        |-decrypt()
        |   Decrypts any files encrypted with the encrypt() method and returns True if successful or the Exception if not.
        |
        |-close()
        |   basically closes the file passed in File(filename) and returns True if successful or the Exception if not.
        .
    '''


    def create(self, name):
        file1 = open(name, 'a')
        return file1
    
    def delete(self, name):
        os.remove(name)
        return True

    def openFile(self, oldName):
        file2 = open(oldName, 'r+')
        return file2
     
    def rename(self, newName):
        os.rename(name, newName)
        return True

    def encrypt(self, name):
        file3 = open(name, 'r').read()
        compression = base64.b64encode(zlib.compress(file3,9))
        file3 = open(name, 'w+')
        file3.write(compression)
        file3.close()
        return True

    def decrypt(self, name):
        file4 = open(name, 'r').read()
        decompression = zlib.decompress(base64.b64decode(file4))
        file4 = open(name, 'w+')
        file4.write(decompression)
        file4.close()
        return True

    def close(self, name):
        name.close()
        return True

    def write(self, File, text):
        File.write(text)
        return True
   












            



            
