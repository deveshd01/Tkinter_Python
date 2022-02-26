from tkinter import *
from tkinter import ttk
import random
from quicksort import quick_sort
from mergesort import merge_sort
from bubbleSort import bubble_sort

root = Tk()
w = root.winfo_screenwidth()
h= root.winfo_screenheight()
C_width = int(w)
C_height = int(h)
root.geometry(f"900x500+{C_width//2-450}+{C_height//2-320}")
root.minsize(900,500)
root.maxsize(900,500)
root.title("  Sorting visualizer  ")
root.config(bg='black')

# varibles
selected_alg = StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left corner
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right corner
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()

def Generate():
    global data

    minVal = int(min_Entry.get())
    maxVal = int(max_Entry.get())
    size = int(size_Entry.get())

    data = []
    for i in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['red' for x in range(len(data))])           #['red', 'red' ,....]

def start_algorithm():
    speed = int(speed_Entry.get() )
    speed = speed/10
    global data

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speed )

    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speed)

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speed)

    drawData(data, ['green' for x in range(len(data))])


frame = Frame(root,width=880,height=300, bg="gray")
frame.grid(row=0,column=0,padx=10,pady=10)

canvas = Canvas(root,width=880,height=380,bg="white")
canvas.grid(row=1,column=0,padx=10,pady=10)

#   VARCHA BOX  (  FRAME  )
Label(frame,text='algorithm : ',bg="gray50",fg='ghost white').grid(row=0,column=0,padx=5,pady=5,sticky=W)
algMenu = ttk.Combobox(frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(2)
Button(frame,text='generated  :  ',command=Generate, bg='bisque2',fg='gray25').grid(row=0,column=2,padx=5,pady=5)
Button(frame,text='start  :  ',command=start_algorithm, bg='bisque2',fg='gray25').grid(row=0,column=3,padx=5,pady=5)

global speed_Entry, size_Entry, max_Entry, min_Entry

Label(frame,text='speed (1-20) : ',bg="gray50",fg='ghost white').grid(row=0,column=4,padx=5,pady=5,sticky=W)
speed_Entry = Entry(frame)
speed_Entry.grid(row=0,column=5,padx=5,pady=5,sticky=W)

Label(frame,text='size : (3-25) ',bg="gray50",fg='ghost white').grid(row=2,column=0,padx=5,pady=5,sticky=W)
size_Entry = Entry(frame)
size_Entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

Label(frame,text='min value (1-10) : ',bg="gray50",fg='ghost white').grid(row=2,column=2,padx=5,pady=5,sticky=W)
min_Entry = Entry(frame)
min_Entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

Label(frame,text='max value (10-100) : ',bg="gray50",fg='ghost white').grid(row=2,column=4,padx=5,pady=5,sticky=W)
max_Entry = Entry(frame)
max_Entry.grid(row=2,column=5,padx=5,pady=5,sticky=W)

root.mainloop()