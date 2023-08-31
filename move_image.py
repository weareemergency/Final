from tkinter import *
from PIL import Image, ImageTk
import time
# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define a Canvas widget
canvas = Canvas(win, width=600, height=400, bg="white")
canvas.pack(padx=20, pady=20)

# Add Images to Canvas widget
imgpath = Image.open('image/기본.png')
image = ImageTk.PhotoImage(imgpath.resize((400, 200)))
img = canvas.create_image(250, 120, anchor=NW, image=image)


def left():
   canvas.move(img, -20, 0)
   time.sleep(1)

def right():
   x = 20
   y = 0
   canvas.move(img, x, y)

def up():
   x = 0
   y = -20
   canvas.move(img, x, y)

def down():
   x = 0
   y = 20
   canvas.move(img, x, y)

# Bind the move function
for imagloop in range(1, 6) :
    left()
    time.sleep(0.5)
    right()
    time.sleep(0.5)
win.mainloop()