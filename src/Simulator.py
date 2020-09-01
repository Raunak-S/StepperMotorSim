import math
import tkinter as tk
from Circle import Circle
import time

addAngle = 1.8 * math.pi/180
circle_list = []
global step
step = 0
radius = 100
global rotating
rotating = 0 

def degreeToRadian(angle):
    return angle*math.pi/180

def rotate(desired_step=0, continuation=0):
    global rotating
    if rotating == 0 and continuation == 0:
        rotating = 1
    elif rotating == 1 and continuation == 0:
        return
    global step
    print(str(step)+","+str(desired_step))
    if step != desired_step:
        for obj in circle_list:
            obj.angle += addAngle
            x = math.cos(obj.angle) * radius + 250
            y = math.sin(obj.angle) * radius + 250
            canvas.coords(obj.circle, x-20, y-20, x+20, y+20)
            canvas.coords(obj.name, x, y)
        step += 1
        L['text']="Step: " + str(step)
        if step == 200: step = 0
        canvas.after(25, rotate, desired_step, 1)
    if step == desired_step:
        #print("Ready to dispense!")
        for i in range(5):
            print(str(step)+","+str(desired_step))
        rotating = 0


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=600)

#txt = canvas.create_text(250, 50, text='around and around')
#canvas.create_rectangle(240, 40, 260, 60, outline="#f11", fill="#1f1", width=2)
#canvas.create_rectangle(240, 240, 260, 260, outline="#f11", fill="#1f1", width=2)
rotatingPlaye = canvas.create_oval(250-150, 250-150, 250+150, 250+150, outline="#f11", fill="#fff", width=2)
dispensingArea = canvas.create_rectangle(math.cos(0)*radius+250-20, math.sin(0)*radius+250-20, math.cos(0)*radius+250+20, math.sin(0)*radius+250+20, outline="#f11", fill="#fff", width=2)
degrees = [0, 59.4, 120.6, 180, 239.4, 300.6]
for i in range(6):
    angle = degreeToRadian(degrees[i])
    start_x = math.cos(angle) * radius + 250
    start_y = math.sin(angle) * radius + 250
    circle = canvas.create_oval(start_x-20, start_y-20, start_x+20, start_y+20, outline="#000", fill="#1f1", width=2)
    text = canvas.create_text(start_x, start_y, text=str(i+1))
    dummy = Circle(text, angle, circle)
    circle_list.append(dummy)

L = tk.Label(root, text="Step: "+str(step), font=('TkDefaultFont', 20))
L.pack()

button = tk.Button(canvas, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.configure(width = 10, activebackground = "#33B5E5", relief = tk.FLAT)
button_window = canvas.create_window(10, 530, anchor=tk.NW, window=button)

button1 = tk.Button(canvas, 
                   text="MED1", 
                   fg="red",
                   command=lambda: rotate(0))
button1.configure(width = 10, activebackground = "#33B5E5", relief = tk.FLAT)
button1_window = canvas.create_window(100, 530, anchor=tk.NW, window=button1)

button2 = tk.Button(canvas, 
                   text="MED2", 
                   fg="red",
                   command=lambda: rotate(167))
button2.configure(width = 10, activebackground = "#33B5E5", relief = tk.FLAT)
button2_window = canvas.create_window(190, 530, anchor=tk.NW, window=button2)

button3 = tk.Button(canvas, 
                   text="MED3", 
                   fg="red",
                   command=lambda: rotate(133))
button3.configure(width = 10, activebackground = "#33B5E5", relief = tk.FLAT)
button3_window = canvas.create_window(280, 530, anchor=tk.NW, window=button3)

button4 = tk.Button(canvas, 
                   text="MED4", 
                   fg="red",
                   command=lambda: rotate(100))
button4.configure(width = 10, activebackground = "#33B5E5", relief = tk.FLAT)
button4_window = canvas.create_window(100, 570, anchor=tk.NW, window=button4)

button5 = tk.Button(canvas, 
                   text="MED5", 
                   fg="red",
                   command=lambda: rotate(67))
button5.configure(width = 10, activebackground = "#33B5E5", relief = tk.FLAT)
button5_window = canvas.create_window(190, 570, anchor=tk.NW, window=button5)

button6 = tk.Button(canvas, 
                   text="MED6", 
                   fg="red",
                   command=lambda: rotate(33))
button6.configure(width = 10, activebackground = "#33B5E5", relief = tk.FLAT)
button6_window = canvas.create_window(280, 570, anchor=tk.NW, window=button6)

canvas.pack()
root.mainloop()
