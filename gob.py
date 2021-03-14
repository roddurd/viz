'''
	This was an assignment for CSCI111 in Fall 2018 at Stetson University. It was originally coded in python3.5 or python3.6. It was updated to python3.9 on 14 March 2021.
'''
'''
    Author: Kathryn Renae Metcalf
    Assignment: Program 4
    Description: Color in a biomorph using a gradient
    Date: 28 September 2018
'''
import tkinter
from tkinter import ttk, Canvas, PhotoImage, mainloop
from tkinter import *
import cmath

WIDTH, HEIGHT = 5000, 5000

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state='normal')

XMIN = -3
XMAX = 3
YMIN = -3
YMAX = 3

c = complex(1.0, 2.0)

for i in range(WIDTH):

    xloc = XMIN + (XMAX - XMIN) * (i/WIDTH)
    # how to get x value from i

    for j in range(HEIGHT):
        yloc = YMIN + (YMAX - YMIN) * (j/WIDTH)
        # how to get y value from j
        z = complex(xloc, yloc)

        while True:
            if abs(z.real) < 10 and abs(z.imag) < 10:
                z = cmath.sin(z) + cmath.exp(z) + c
            else:
                break

        red = int(abs(z.real)) * 5
        green = int(abs(z.real + z.imag))
        blue = int(abs(z.imag)) * 30

        if red <= 255:
            red = '{0:0{1}x}'.format(red,2)
        else:
            red = int(red / 5000)
            red = '{0:0{1}x}'.format(red,2)

        if green <= 255:
            green = '{0:0{1}x}'.format(green,2)
        else:
            green = int(green / 5000)
            green = '{0:0{1}x}'.format(green,2)

        if blue <= 255:
            blue = '{0:0{1}x}'.format(blue,2)
        else:
            blue = int(blue / 5000)
            blue = '{0:0{1}x}'.format(blue,2)

        colr = '#' + red + green + blue

        img.put(colr, (i,j))

mainloop()
