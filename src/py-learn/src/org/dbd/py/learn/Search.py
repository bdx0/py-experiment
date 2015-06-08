# Below is the API the getInfo function uses. 
# http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=
import json
import urllib
from BeautifulSoup import BeautifulSoup
from Tkinter import *
import tkMessageBox as msg


def getInfo():

    # Retrieves the text entered in to the query widget then encodes it
    # in to text the browser can read eg 'hello there' converted in to 'hello%20there'
    query = queryVar.get()
    encodedQuery = urllib.quote(query)

    # Builds the string URL with the encoded text from the query widgit. At the same time the
    # urllib opens the URL and reads the html containg json data
    rawData = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + encodedQuery).read()

    # Uses the json module to load jason data and find data in the fields responsesData and results
    # Results contian the links to the websites.
    jsonData = json.loads(rawData)
    searchResults = jsonData['responseData']['results']

    # deletes any existing text in the text widgit so the program doesn't overload with text from
    # multiple query's
    textDisplay.delete(1.0, END)
    
    # loops through the API json results data to retrieve the webpage link and title
    for result in searchResults:
        link = result['url']
        
        # opens the link in the urllib and reads the page source. Then sets up a beautiful soup
        # to easily extract body text in the source to display to the user.
        pageData = urllib.urlopen(link).read()
        soup = BeautifulSoup(pageData)

        # Finds the title of the current webpage in the beautiful soup module
        titleText = soup.find('title')
        
        
        # Inserts the link to the current website then seperates the page title with
        # a blank line to make the info more readable.
        textDisplay.insert(INSERT, 'URL:' + link + '  ')
        textDisplay.insert(INSERT, titleText.text)
        textDisplay.insert(INSERT, '\n')
        textDisplay.insert(INSERT, '\n')
       
        # loops through the data extracted by the beautiful soup module. The text.text makes sure that the
        # data in the soup.find_all('p') contains no html tags. After removing all tags it inserts the data
        # in to the textDisplay widget.
        for text in soup.find_all('p'):
            bodyText = text.text
            textDisplay.insert(END, bodyText)

        # below sets up message that shows us that the current website data has ended
        textDisplay.insert(END, '\n')
        textDisplay.insert(END, '**************************************END***************************************')
        textDisplay.insert(END, '\n')

    # Updates the text widget with all the new web page data.       
    textDisplay.grid(row=3, column=1) 

# basic tkinter GUI set up
root = Tk()
root.title('Article Grab by Nicholas Cannon')
root.geometry('582x455')
root.configure(background='light grey')

# Frame will contain all the widgets and will use grid as the geometry manager
frame = Frame(root, bd=2, bg='light grey')
frame.grid()

# creates and modifies the text widgit to suit the rest of the gui 
textDisplay = Text(frame, bg='white', fg='Black', bd=5)
textDisplay.config(highlightbackground='grey')
textDisplay.insert(INSERT, 'Enter a word or phrase in the query bar above to get info here!')
textDisplay.grid(row=3, column=1)

# Sets up the Entry widgit to store the text in to the queryVar variable 
queryVar = StringVar()
queryWidgit = Entry(frame, textvariable=queryVar, fg='Blue', bd=5, width=50)
queryWidgit.config(highlightbackground='light grey')
queryWidgit.insert(0, 'Enter query here!')
queryWidgit.grid(row=1, column=1, columnspan=2)

# creates button that runs the getInfo() function which recieves all the web data
button = Button(frame, bg='dark grey', command=getInfo, width=10, text='Search')
button.config(highlightbackground='light grey')
button.grid(row=2, column=1)

# Label to show which google API the program uses
label2 = Label(frame, bg='light grey', text='Powered by ajax.googleapis.com search API')
label2.grid(row=4, column=1)

# starts the tkinter mainloop
root.mainloop()



