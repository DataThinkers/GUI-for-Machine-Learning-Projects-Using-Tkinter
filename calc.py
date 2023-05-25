from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root =Tk()

root.title("Calculator")

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

label= Label(root,text="Enter First Number",bg="lightblue",foreground="black",
             font=("Arial",15,"bold"))
label.pack()

first_no = Entry(root,width=15,font=("Arial",14),bg="gray",fg="white",borderwidth=3)
first_no.pack(pady=5)


label= Label(root,text="Enter Second Number",bg="lightblue",foreground="black",
             font=("Arial",15,"bold"))
label.pack()
second_no = Entry(root,width=15,font=("Arial",14),bg="gray",fg="white",borderwidth=3)
second_no.pack(pady=5)

result_label= Label(root,text="Result",bg="lightblue",foreground="black",
             font=("Arial",15,"bold"))
result_label.pack()

def calc():
    no1 = float(first_no.get())
    no2 = float(second_no.get())

    result = no1 + no2
    result_label.config(text="Result: " + str(result))



my_button=Button(text="Add",bg="lightgreen",activebackground="blue",
                 borderwidth=3,font=("Arial",11,"bold"),command=calc)
my_button.pack(pady=10)




root.mainloop()


