from Tkinter import *

root= Tk()
root.title("GUI Window")
root.geometry("200x100")

app = Frame(root)
app.grid()
button1 = Button(app, text= "My button").grid()
label = Label(app, text="This is my window")
label.grid()

root.mainloop()

