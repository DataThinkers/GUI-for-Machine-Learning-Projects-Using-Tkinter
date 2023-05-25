from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib

iris = load_iris()

X = iris.data
y = iris.target

model = DecisionTreeClassifier()
model.fit(X,y)


joblib.dump(model,"iris_model.joblib")

root =Tk()

root.title("Iris Flower Predictor")

root.geometry("300x500")

root.configure(bg="lightblue")
image = Image.open("C:\\Users\\SFL-3\\tkinter1\\venv\\logo.png")

resized_image = image.resize((100,100))

photo= ImageTk.PhotoImage(resized_image)

label = Label(root,image=photo)
label.pack(pady=10)

label1= Label(root,text="Sepal Length",bg="lightblue",foreground="black",
             font=("Arial",15,"bold"))
label1.pack()

entry1 = Entry(root,width=10,font=("Arial",14),bg="gray",fg="white",borderwidth=3)
entry1.pack(pady=5)
##########################################################################
label2= Label(root,text="Sepal Width",bg="lightblue",foreground="black",
             font=("Arial",15,"bold"))
label2.pack()

entry2 = Entry(root,width=10,font=("Arial",14),bg="gray",fg="white",borderwidth=3)
entry2.pack(pady=5)

############################################################################
label3= Label(root,text="Petal Length",bg="lightblue",foreground="black",
             font=("Arial",15,"bold"))
label3.pack()

entry3 = Entry(root,width=10,font=("Arial",14),bg="gray",fg="white",borderwidth=3)
entry3.pack(pady=5)
###############################################################################
label4= Label(root,text="Petal Width",bg="lightblue",foreground="black",
             font=("Arial",15,"bold"))
label4.pack()

entry4 = Entry(root,width=10,font=("Arial",14),bg="gray",fg="white",borderwidth=3)
entry4.pack(pady=5)
##############################################################################
species_label= Label(root,text="",bg="lightblue",foreground="black",
             font=("Arial",15,"bold"))
species_label.pack()

model = joblib.load("iris_model.joblib")

def predict_species():
    sepal_length = float(entry1.get())
    sepal_width = float(entry2.get())
    petal_length = float(entry3.get())
    petal_width = float(entry4.get())

    prediction = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
    species_label.config(text="Predicted Species: "+iris.target_names[prediction[0]])

my_button=Button(text="Add",bg="lightgreen",activebackground="blue",
                 borderwidth=3,font=("Arial",11,"bold"),command=predict_species)
my_button.pack(pady=10)




root.mainloop()