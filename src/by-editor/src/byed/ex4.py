#Text Config 2
#Created By Nicholas Cannon

from Tkinter import * 
import tkMessageBox as msg
import fileMechanics as fm
import tkFileDialog
import syntaxHighlighting as sh

saved = False
global currentFile
currentFile = 'Untitled'
counter = 0

def backspaceCount():
    global counter
    counter -= 1
    if counter < 0:
        counter = 0
    return

def count():
    global counter
    counter += 1
    return

def syntax(key, display, totalIndex):
    sh.callback(key, display, totalIndex)

def handler():
    if saved == False:
        option = msg.askyesno(title='Text Config 2', message='Do you want to save before '\
                            + 'you quit?')
        if option:
            save(f, display)
            root.destroy()
            
        else:
            root.destroy()
            
    else:
        save(f, display)
        root.destroy()
        

def Open(f, display):
    global saved
    global File
    try:
        File = tkFileDialog.askopenfilename(title='Open File')
        opened = f.openFile(File)
        
        currentFile = File
        root.title(currentFile)
        
        data = opened.read()
        display.insert(INSERT, str(data))
        saved = True
    except Exception, e:
        msg.showinfo(title='Error',  message='Error opening file ' \
                     + File + '. ' + str(e))
        

def new(f):
    global saved
    global File
    try:
        File = tkFileDialog.asksaveasfilename(title='New File')
        f.create(File)
        currentFile = File
        root.title(currentFile)
        saved = True

    except Exception, e:
        msg.showinfo(title='Error',  message='Error creating file ' + File\
                     + '. ' + str(e))
        

def save(f, display):
    global File
    global saved
    if saved == False:
        File = tkFileDialog.asksaveasfilename(title='Save File')
        
        if File == '':
            return None
        try:
            file1 = f.create(File)
            f.write(file1, display.get(1.0, END))
            f.close(file1)
            currentFile = File
            root.title(currentFile)
            saved = True
            
        except Exception, e:
            msg.showinfo(title='Error',  message='Error writing to file. ' + str(e))
            
    if saved:
        try:
            file1 = f.openFile(File)
            f.write(file1, display.get(1.0, END))
            f.close(file1)
            saved = True
            msg.showinfo(title='Success!', message='Successfully saved to ' + File)
        except Exception, e:
            msg.showinfo(title='Error',  message='Error writing to file. ' + str(e))
 
        return True

def saveAs(f, display):
    global saved
    saved = False
    save(f, display)


f = fm.File()


#Window set up below
global root
root = Tk()
root.geometry('360x450')
root.title(currentFile)

display = Text(root, height=30, width=50, wrap=WORD)
display.pack(fill=BOTH, expand=True)

root.bind('<Command-s>', lambda x: save(f, display))
root.bind('<Command-n>', lambda z: new(f))
root.bind('<Command-o>', lambda y: Open(f, display))
root.bind('<Command-q>', lambda c: handler())
root.bind('<space>', lambda b: syntax(display.get(1.0, END), display, counter))
root.bind('<Key>', lambda c: count())
root.bind('<BackSpace>', lambda a: backspaceCount())
    

menu = Menu(root)
filemenu = Menu(menu)

filemenu.add_command(label=u'New \u2318N', command=lambda:new(f))
filemenu.add_command(label=u'Open \u2318O', command=lambda:Open(f, display))
filemenu.add_command(label=u'Save \u2318S', command=lambda:save(f, display))
filemenu.add_command(label='Save as...', command=lambda:saveAs(f, display))
filemenu.add_command(label=u'Exit \u2318Q', command=root.destroy)

menu.add_cascade(label='File', menu=filemenu)
root.config(menu=menu)

root.protocol("WM_DELETE_WINDOW", handler)

root.mainloop()
