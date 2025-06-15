from tkinter import *   

w = Tk()
w.title("Top Window Example")
w.geometry("300x200")

def top_win():
    top = Toplevel(w)
    top.title("Top window")
    top.geometry("200x100")
    l2 = Label(top, text="This is a top window")
    l2.pack()

    top_win.mainloop()

l1 = Label(w,text= "This is the main window")
btn = Button(w, text="Open" , command=top_win)

l1.pack()
btn.pack()

w.mainloop()
