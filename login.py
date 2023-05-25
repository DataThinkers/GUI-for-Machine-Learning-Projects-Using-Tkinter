from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root =Tk()

root.title("Login")


root.geometry("600x400")

root.minsize(200,200)

root.maxsize(300,700)


root.iconbitmap("C:\\Users\\SFL-3\\tkinter1\\venv\\logo.ico")

root.configure(bg="lightblue")

image = Image.open("C:\\Users\\SFL-3\\tkinter1\\venv\\logo.png")

resized_image = image.resize((100,100))

photo= ImageTk.PhotoImage(resized_image)

label = Label(root,image=photo)
label.pack(pady=10)

label= Label(root,text="Enter Username",bg="lightblue",foreground="black",font=("Arial",15,"bold"))
label.pack()

username = Entry(root,width=20,font=("Arial",14),bg="gray",fg="white",borderwidth=3)
username.pack(pady=5)

label= Label(root,text="Enter Password",bg="lightblue",foreground="black",font=("Arial",15,"bold"))
label.pack()

password = Entry(root,width=20,font=("Arial",14),bg="gray",fg="white",borderwidth=3,show="*")
password.pack(pady=5)

def login():
    username1 = username.get()
    password1 = password.get()
    if username1 =="admin" and password1 =="password":
        messagebox.showinfo("Login","Login Successful")
    else:
        messagebox.showerror("Fail","Invalid Username or Password")


my_button=Button(text="Login",bg="lightgreen",activebackground="blue",
                 borderwidth=3,font=("Arial",11,"bold"),command=login)
my_button.pack(pady=10)


root.mainloop()