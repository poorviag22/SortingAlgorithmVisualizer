import imp
from tkinter import *
from tkinter import ttk

# We will need random to create array
import random
 
# Importing colors from colors.py that we made earlier
from color import *

from algorithms.bubbleSort import bubble_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.insertionSort import insertion_sort
from algorithms.selectionSort import selection_sort

# Creating a basic window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1300, 700)
window.config(bg=LIGHT_GRAY)

algorithm_name= StringVar()
algolist=['Bubble Sort','Merge Sort','Quick Sort','Insertion Sort','Selection Sort']
speed_name=StringVar()
speedlist=['Fast','Medium','Low']

data=[]
 
def drawData(data,colorArray):
    canvas.delete("all")
    canvas_width=1000
    canvas_height=400
    xwidth=canvas_width/(len(data)+1)   # gives width of bar
    offset=12
    spacing=3
    normalizedData=[i/max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * xwidth + offset + spacing
        y0 = canvas_height - height * 350
        x1=(i+1)*xwidth+offset
        y1=canvas_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
    
    window.update_idletasks()  #enter event loop until all idle callbacks have been called
def generate():

    global data
    data=[]
    for i in range(0,80):
        random_value=random.randint(1,100)
        data.append(random_value)

    drawData(data,[BLUE for x in range(len(data))])  

def set_speed():
    if speedmenu.get()=='Low':
        return 0.5

    elif speedmenu.get()=='Medium':
         return 0.1
    else:
        return 0.001

def sort():
    global data
    timeTick=set_speed()

    if algomenu.get()=='Bubble Sort':
        bubble_sort(data,drawData,timeTick)

    elif algomenu.get()=='Merge Sort':
        merge_sort(data,0,len(data)-1,drawData,timeTick)

    elif algomenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick)  

    elif algomenu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)  

    else:
        selection_sort(data, drawData, timeTick)             

                    ### user interface###
uiframe=Frame(window,width=900,height=300,bg=LIGHT_GRAY)
uiframe.grid(row=0,column=0,padx=500,pady=50)

l1=Label(uiframe,text="Algorithm: ",bg=LIGHT_GRAY)
l1.grid(row=0,column=0,padx=10,pady=5,sticky=W)
algomenu=ttk.Combobox(uiframe,textvariable=algorithm_name,values=algolist)
algomenu['state']='readonly'
algomenu.grid(row=0,column=1,padx=5,pady=5)
algomenu.current(0)

l2=Label(uiframe,text="Sorting Speed: ",bg=LIGHT_GRAY)
l2.grid(row=1,column=0,padx=10,pady=5,sticky=W)
speedmenu=ttk.Combobox(uiframe,textvariable=speed_name,values=speedlist)
speedmenu['state']='readonly'
speedmenu.grid(row=1,column=1,padx=5,pady=5)
speedmenu.current(0)

b1=Button(uiframe,text="Sort",command=sort,bg=DARK_GRAY)
b1.grid(row=2,column=1,padx=10,pady=10)

b3=Button(uiframe,text="Generate Array",command=generate,bg=DARK_GRAY)
b3.grid(row=2,column=0,padx=10,pady=10)

canvas=Canvas(window,width=1000,height=400,bg=LIGHT_GRAY)
canvas.grid(row=1,column=0,padx=1,pady=5)


window.mainloop()  #for running application
