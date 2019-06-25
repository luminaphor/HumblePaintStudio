from tkinter import *
from tkinter import ttk
from tkinter import filedialog,messagebox
from PIL import ImageGrab

width=900
height=800
x,y=0,0 #initializes cursor

BLACK="#000000"
RED="#FF0000"
GREEN="#008000"
BLUE="#0000FF"
WHITE="#FFFFFF"

ACTIVE_COLOR=WHITE
PEN_SIZE=1.0

def getXY(event): #gets current position of cursor
    global x,y
    x,y=event.x,event.y

def draw(event): #creates a line with length of initial x,y values to x,y at time of keypress. Also uses current active color and pen size.
    global x,y,ACTIVE_COLOR,PEN_SIZE
    CANVAS.create_line((x,y,event.x,event.y),fill=ACTIVE_COLOR,width=PEN_SIZE)
    x,y=event.x,event.y

def setColor(newColor): #allows current active color to be changed
    global ACTIVE_COLOR
    ACTIVE_COLOR=newColor
    return ACTIVE_COLOR
  
def erase(event): #change pen to eraser on right-click
    global ACTIVE_COLOR
    ACTIVE_COLOR=WHITE
    print("Active color set to erase")
    return ACTIVE_COLOR

def setSize(size): #changes size of pen based on slider
    global PEN_SIZE
    PEN_SIZE=size
    return PEN_SIZE

def clearCanvas(event): #clears whole canvas
    print("cleared")
    CANVAS.create_line((0,0,1000,1000),fill=WHITE,width=2000)

def exitProgram(event): 
    root.destroy()

def saveProgram(event): #uses PIL imagegrab function to grab the root window and crop based on the dimensions output by getDimensions function, Saves as png.
    filename=filedialog.asksaveasfilename()
    topx,topy,botx,boty=getDimensions(CANVAS)
    ImageGrab.grab().crop([topx,topy,botx,boty]).save(filename+'.png',format='png')

def getDimensions(widget): #gets the dimensions of the actual canvas inside canvas container
    topx=CANVAS_CONTAINER.winfo_rootx()+widget.winfo_x()
    topy=CANVAS_CONTAINER.winfo_rooty()+widget.winfo_y()
    botx=topx+widget.winfo_width()
    boty=topy+widget.winfo_height()
    return topx,topy,botx,boty

#initializing components of GUI
root=Tk() 
root.title("Humble Paint Studio")
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

#import png images for color palette. 
black_icon=PhotoImage(file='crayonbox\\black.png')
white_icon=PhotoImage(file='crayonbox\\white.png')
blue_icon=PhotoImage(file='crayonbox\\blue.png')
green_icon=PhotoImage(file='crayonbox\\green.png')
red_icon=PhotoImage(file='crayonbox\\red.png')

#my crayon box. The buttons that allow the color of the pen to be changed. Also assigns each its respective icon.
BLACK_PEN=ttk.Button(CRAYON_BOX,command=lambda: setColor(BLACK),image=black_icon)
BLACK_PEN.grid_configure(column=0,row=1,sticky=W)

RED_PEN=ttk.Button(CRAYON_BOX,command=lambda: setColor(RED),image=red_icon)
RED_PEN.grid_configure(column=0,row=2,sticky=W)

GREEN_PEN=ttk.Button(CRAYON_BOX,command=lambda: setColor(GREEN),image=green_icon)
GREEN_PEN.grid_configure(column=0,row=3,sticky=W)

BLUE_PEN=ttk.Button(CRAYON_BOX,command=lambda: setColor(BLUE),image=blue_icon)
BLUE_PEN.grid_configure(column=0,row=4,sticky=W)

#other options outside of color palette
#allows for pen to be resized.
RESIZE_LABEL=Label(CANVAS_CONTAINER,text="Pen Size")
RESIZE_LABEL.grid(column=1,row=0,sticky=W)

RESIZE=ttk.Scale(CANVAS_CONTAINER,orient=HORIZONTAL,length=900,from_=1.0,to=50,command=lambda size: setSize(size))
RESIZE.grid(column=1,row=1,sticky=E)

#executes the clearscreen, save, and exit functions
CLEAR_BUTTON=ttk.Button(OPTIONS_MENU,text="CLEAR")
CLEAR_BUTTON.grid_configure(column=3,row=6,sticky=E)
CLEAR_BUTTON.bind("<Button-1>",clearCanvas)

SAVE_BUTTON=ttk.Button(OPTIONS_MENU,text="SAVE")
SAVE_BUTTON.grid_configure(column=4,row=6,sticky=E)
SAVE_BUTTON.bind("<Button-1>",saveProgram)

EXIT_BUTTON=ttk.Button(OPTIONS_MENU,text="EXIT")
EXIT_BUTTON.grid_configure(column=5,row=6,sticky=E)
EXIT_BUTTON.bind("<Button-1>",exitProgram)

#the actual canvas
CANVAS=Canvas(CANVAS_CONTAINER,width=width,height=height,bg="white")
CANVAS.grid_configure(column=1,row=2,sticky=(N,W,E,S))

#canvas event bindings. allows for drawing. 
CANVAS.bind("<Button-1>",getXY)
CANVAS.bind("<B1-Motion>",draw)
CANVAS.bind("<Button-3>",erase)

#assemble the workspace!
for child in mainWindow.winfo_children(): 
    child.grid_configure(padx=5,pady=5)

root.mainloop()

