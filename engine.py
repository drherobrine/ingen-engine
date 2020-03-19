from tkinter import *
from Sprite import *

cwidth = 640
cheight = 360
frame = 0
fps = 0
tk = Tk()
canvas = Canvas(tk, width=cwidth, height=cheight)
canvas.pack()
bop = Sprite.Sprite(320, 180, [], canvas, "bop")
tk.mainloop()