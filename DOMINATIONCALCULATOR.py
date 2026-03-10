from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Domination Calculator')
root.geometry('400x400')
root.configure(bg='lightblue')

upload = Image.open("image.jpg")

upload = upload.resize((200, 200))
image = ImageTk.PhotoImage(upload)
img_label = Label(root, image=image, bg='lightblue')
img_label.place(x=100, y=20)

lable1 = Label(root, text="Hey User! Welcome to the Domination Calculator", bg='lightblue', font=('Arial', 12))
lable1.place(x=50, y=230, anchor='center')

def msg():
    MsgBox = messagebox.askquestion("Alert", "Do you want to calculate your domination?")
    if MsgBox == 'yes':
        messagebox.showinfo("Domination Calculator", "Calculating your domination...")
        topwin()

button1 = Button(root, text="Lets get started!", command=msg, bg='blue', fg='white', font=('Arial', 10))
button1.place(x=150, y=300)

def topwin():
    top = Toplevel()
    top.title("Currency Domination Counter")
    top.configure(bg='lightblue')
    top.geometry('400x400')
    
    label = Label(top , text="Enter Amount", bg='lightblue', font=('Arial', 12))
    label.place(x=50, y=50)

    entry = Entry(top, width=20)
    entry.place(x=150, y=50)

    lbl = Label(top, text="Domination Breakdown", bg='lightblue', font=('Arial', 12))
    lbl.place(x=50, y=100)

    l1 = Label(top, text="1000: ", bg='lightblue', font=('Arial', 10))
    l1.place(x=50, y=150)

    l2 = Label(top, text="500: ", bg='lightblue', font=('Arial', 10))
    l2.place(x=50, y=180)

    l3 = Label(top, text="100: ", bg='lightblue', font=('Arial', 10))
    l3.place(x=50, y=210)

    t1 = Label(top, text="0: ", bg='lightblue', font=('Arial', 10))
    t1.place(x=150, y=150)

    t2 = Label(top, text="0: ", bg='lightblue', font=('Arial', 10))
    t2.place(x=150, y=180)

    t3 = Label(top, text="0: ", bg='lightblue', font=('Arial', 10))
    t3.place(x=150, y=210)

    def calculate():
        try:
            amount = int(entry.get())

            domination_1000 = amount // 1000
            domination_500 = amount // 500
            domination_100 = amount // 100

            t1.config(text=str(domination_1000))
            t2.config(text=str(domination_500))
            t3.config(text=str(domination_100))

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer amount.")

    btn = Button(top, text="Calculate", command=calculate, bg='blue', fg='white', font=('Arial', 10))
    btn.place(x=150, y=300)

    top.mainloop()

root.mainloop()