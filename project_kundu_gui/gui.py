from Tkinter import *

root = Tk()

frame = Frame(root)

frame.grid()
b1= Button(frame, text="But 1")
b2= Button(frame, text="But 2")
b3= Button(frame, text="But 3")
b4= Button(frame, text="But 4")
b1.pack()
b2.pack()
b3.pack()
b4.pack()
root.mainloop()

