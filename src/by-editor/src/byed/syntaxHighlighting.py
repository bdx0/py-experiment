#Text config 2
#created by Nicholas Cannon
import re
mainText = ''

def callback(text, display, totalIndex):
    #global mainText
    

    display.tag_config('orange', foreground='dark orange')
    display.tag_config('blue', foreground='blue')
    display.tag_config('red', foreground='red')
    display.tag_config('purple', foreground='purple')
    display.tag_config('green', foreground='green')
    display.tag_config('normal', foreground='black')
        
    #if 'import' or 'def' or 'if' or 'elif' or 'else' or 'or' or 'and' or 'as' or 'try' or 'except' or 'in' or 'global' or 'lambda' in mainText:

    textList = text.split(' ')
    print textList

    indexCount = -1
    for item in textList:
        indexCount += 1

        if 'import' in item:
            startIndex = totalIndex - 5
            print 'start: ' + str(startIndex)
            print 'end: ' + str(totalIndex)
            display.tag_add('orange', float(startIndex), float(totalIndex))
            print 'found'


        print indexCount
        print textList
