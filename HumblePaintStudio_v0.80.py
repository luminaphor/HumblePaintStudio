from tkinter import *
from tkinter import ttk
from tkinter import filedialog,messagebox
import PIL

#initializes cursor
x,y=0,0

#gets the current x and y position of cursor 
def getXY(event):
    global x,y
    x,y=event.x,event.y

#gets the current x and y position of cursor and draws a corresponding line
#def draw(event):
#    global x,y,ACTIVE_COLOR,PEN_SIZE
#    CANVAS.create_line((x,y,event.x,event.y),fill=ACTIVE_COLOR,width=PEN_SIZE)
#    x,y=event.x,event.y

def draw(event):
    global x,y,ACTIVE_COLOR,PEN_SIZE
    CANVAS.create_line((x,y,event.x,event.y),fill=ACTIVE_COLOR,width=PEN_SIZE)
    x,y=event.x,event.y

#is SUPPOSED TO change the current active_color to the one corresponding to whichever button is selected
#but that doesn't seem to be happening for some reason
def setColor(newColor):
    global ACTIVE_COLOR
    ACTIVE_COLOR=newColor
    #print("COLOR WAS CHANGED TO {}".format(newColor))
    return ACTIVE_COLOR
  
def erase(event):
    global ACTIVE_COLOR
    ACTIVE_COLOR=ERASER
    print("Active color set to erase")
    return ACTIVE_COLOR

def setSize(size):
    global PEN_SIZE
    PEN_SIZE=size
    return PEN_SIZE

def clearCanvas(event):
    print("cleared")
    CANVAS.create_line((0,0,1000,1000),fill=ERASER,width=2000)

def exitProgram(event):
    root.destroy()

#does absolutely nothing... Some people MIGHT get upset by that.
def saveProgram(event):
    filename=filedialog.asksaveasfilename()
    messagebox.showinfo(message="Are you sure you want to save {}?".format(filename),type="yesno")

#the components making up my application
root=Tk()
root.title("Semi-Adequate Paint Studio")
root.columnconfigure(0,weight=10)
root.rowconfigure(0,weight=10)

mainWindow=ttk.Frame(root,padding="3 3 12 12")
mainWindow.grid(sticky=(N,W,E,S))

CRAYON_BOX=ttk.Frame(mainWindow,padding=3,borderwidth=5,relief="sunken")
CRAYON_BOX.grid_configure(column=0,row=2,rowspan=1,columnspan=1,sticky=W)

CANVAS_CONTAINER=ttk.Frame(mainWindow,padding=1,borderwidth=5,relief="groove")
CANVAS_CONTAINER.grid_configure(column=1,row=2,columnspan=2,sticky=N)

OPTIONS_MENU=ttk.Frame(mainWindow,padding=1,borderwidth=5,relief="groove")
OPTIONS_MENU.grid_configure(column=2,row=3,sticky=E)

#default colors- ill expand on this later
BLACK="#000000"
RED="#FF0000"
GREEN="#008000"
BLUE="#0000FF"
ERASER="#FFFFFF"

black_icon=PhotoImage(file='HumblePaintStudio\\crayonbox\\black.png')
white_icon=PhotoImage(file='HumblePaintStudio\\crayonbox\\white.png')
blue_icon=PhotoImage(file='HumblePaintStudio\\crayonbox\\blue.png')
green_icon=PhotoImage(file='HumblePaintStudio\\crayonbox\\green.png')
red_icon=PhotoImage(file='HumblePaintStudio\\crayonbox\\red.png')

#current active color for use in variable/value comparisons
ACTIVE_COLOR=ERASER
PEN_SIZE=5.0

#my crayon box
BLACK_PEN=ttk.Button(CRAYON_BOX,command=lambda: setColor(BLACK),image=black_icon)
BLACK_PEN.grid_configure(column=0,row=1,sticky=W)
#BLACK_PEN.bind("<Button-1>",setColor)

RED_PEN=ttk.Button(CRAYON_BOX,command=lambda: setColor(RED),image=red_icon)
RED_PEN.grid_configure(column=0,row=2,sticky=W)
#RED_PEN.bind("<Button-1>",setColor)
#RED_PEN['command']=setColor("red")

GREEN_PEN=ttk.Button(CRAYON_BOX,command=lambda: setColor(GREEN),image=green_icon)
GREEN_PEN.grid_configure(column=0,row=3,sticky=W)
#GREEN_PEN['command']=setColor("green")

BLUE_PEN=ttk.Button(CRAYON_BOX,command=lambda: setColor(BLUE),image=blue_icon)
BLUE_PEN.grid_configure(column=0,row=4,sticky=W)
#BLUE_PEN['command']=setColor("blue")

RESIZE_LABEL=Label(CANVAS_CONTAINER,text="Pen Size")
RESIZE_LABEL.grid(column=1,row=0,sticky=W)

RESIZE=ttk.Scale(CANVAS_CONTAINER,orient=HORIZONTAL,length=900,from_=1.0,to=50,command=lambda size: setSize(size))
RESIZE.grid(column=1,row=1,sticky=E)

CLEAR_BUTTON=ttk.Button(OPTIONS_MENU,text="CLEAR")
CLEAR_BUTTON.grid_configure(column=3,row=6,sticky=E)
CLEAR_BUTTON.bind("<Button-1>",clearCanvas)

SAVE_BUTTON=ttk.Button(OPTIONS_MENU,text="SAVE")
SAVE_BUTTON.grid_configure(column=4,row=6,sticky=E)
SAVE_BUTTON.bind("<Button-1>",saveProgram)

EXIT_BUTTON=ttk.Button(OPTIONS_MENU,text="EXIT")
EXIT_BUTTON.grid_configure(column=5,row=6,sticky=E)
EXIT_BUTTON.bind("<Button-1>",exitProgram)

#my canvas. will probably change this later to something more suitable.
CANVAS=Canvas(CANVAS_CONTAINER,width=900,height=800,bg="white")
CANVAS.grid_configure(column=1,row=2,sticky=(N,W,E,S))

CANVAS.bind("<Button-1>",getXY)
CANVAS.bind("<B1-Motion>",draw)
CANVAS.bind("<Button-3>",erase)

#assemble the workspace!
for child in mainWindow.winfo_children(): 
    child.grid_configure(padx=5,pady=5)

#will be used to check for keystrokes and button presses
root.mainloop()

