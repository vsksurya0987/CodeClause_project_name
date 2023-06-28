from tkinter import *
from tkinter.filedialog import *

filename = None

# create new file
def newFile():
    global filename
    filename = "Just Write"
    text.delete(0.0, END)

# save file
def saveFile():
    global filename
    # left: line number ; right: column number
    t = text.get(0.0, END)

    # opens file with filename
    f = open(filename, 'w')
    f.write(t)
    f.close()
    
# save as new file
def saveAs():
    # defaultExtension automatically makes it a txt file
    f = asksaveasfile(defaultextension = '.txt')
    t = text.get(0.0, END)

    # rstrip = cut the white spaces beneath the written files
    try:
        f.write(t.rstrip())

    except:
        showerror(title = "Oops!", message = "Unable to save file :(")

# open a file
def openFile():
    global filename #newline
    f = askopenfile(parent = root, title = 'Select a File') #modifiedline
    filename = f.name
    #f = askOpenFile(mode = 'r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    f.close() #newline

# writing tkinter part
# our main window, root
root = Tk()

# name of program, sizes
root.title("My Morning Pages")
root.minsize(width = 400, height = 400)
root.maxsize(width = 800, height = 800)

text = Text(root, width = 400, height = 400)
text.pack()

# create a menu bar
menubar = Menu(root)
filemenu = Menu(menubar)

# command buttons and options
filemenu.add_command(label = "New", command = newFile)
filemenu.add_command(label = "Open", command = openFile)
filemenu.add_command(label = "Save", command = saveFile)
filemenu.add_command(label = "Save As...", command = saveAs)

filemenu.add_separator()
filemenu.add_command(label = "Quit", command = root.quit)

# add cascade style
menubar.add_cascade(label = "File", menu = filemenu)

root.config(menu = menubar)
root.mainloop()
