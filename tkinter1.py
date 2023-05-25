from tkinter import *
from tkinter import messagebox
root = Tk()

root.title("My Title")

root.geometry("400x300")

root.minsize(200,200)

root.maxsize(600,600)

root.iconbitmap("C:\\Users\\SFL-3\\tkinter1\\venv\\logo.ico")

root.configure(bg="lightblue")

label = Label(root,text="Hello,Tkinter!!!",
              font=("Arial",20,"bold"),
              bg="lightblue",foreground="yellow")
label.pack(side=TOP)

my_entry=Entry(root,width=30,font=("Arial",14),bg="gray",fg="white",
               borderwidth=3,show="*")
my_entry.pack()

def test():
    messagebox.showerror("Info","Button Clicked!!!")

my_button=Button(text="Click Me!!!",command=test,bg="pink",font=("Arial",20,"bold"),
                 borderwidth=3,activebackground="blue")
my_button.pack(pady=10)

options = ["Option 1","Option 2","Option 3"]

selected_option = StringVar()

selected_option.set(options[0])

option_menu=OptionMenu(root,selected_option,*options)
option_menu.configure(bg="green",fg="white",font=("Arial",12),width=15)
option_menu["menu"].config(bg="green",fg="white",font=("Arial",12))
option_menu.pack()





root.mainloop()





