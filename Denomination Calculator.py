from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

w = Tk()
w.title("Denomination Calculator")
w.geometry("500x350")
w.config(bg = "cyan")

upload = Image.open("app_img.jpg")

upload = upload.resize((500, 350), Image.ANTIALIAS)
img = ImageTk.PhotoImage(upload)
Label (w , image=img).place(x=0, y=0)

Label1 = Label(w, text="Welcome to the Denomination Calculator", bg="cyan", font=("Arial", 14))
Label1.place(x=10, y=10)

def msg():
    magbox = messagebox.showinfo("Do you Want to continue?", "This is a simple denomination calculator.\n")
    if magbox == "ok":
        top_win()


button = Button(w , text="Let's Start" , command=msg, bg="blue", fg="white", font=("Arial", 12))
button.place(x=10, y=50)

def top_win():
    top = Toplevel(w)
    top.title("Denomination Calculator")
    top.geometry("400x300")
    top.config(bg="cyan")

    label = Label(top , text="Enter Total Amount:", bg="cyan", font=("Arial", 12))
    entry = Entry(top)
    lbl = Label(top , text="Here is the denomination breakdown:", bg="cyan", font=("Arial", 12))

    l1 = Label(top , text="2000:")
    l2 = Label(top , text="500:")
    l3 = Label(top , text="200:")

    e1 = Entry(top)
    e2 = Entry(top)
    e3 = Entry(top)
     
    def calculate():
        try:
            global amount
            amount = int(entry.get())

            n2000 = amount // 2000
            amount %= 2000
            n500 = amount // 500
            amount %= 500
            n200 = amount // 100   
            amount %= 100

            


