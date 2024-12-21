from tkinter import *

root = Tk()
root.title("Inches to Centimeters Converter")
root.geometry('300x200')

label1 = Label(root, text="Enter length in inches:")
label1.place(x=20, y=50)

e1 = Entry(root)
e1.place(x=150, y=50)

def convert_to_cm():
    inches = float(e1.get())
    cm = inches * 2.54
    result_label.config(text="Length in cm: " + str(cm))

result_label = Label(root, text="")
result_label.place(x=50, y=120)

b1 = Button(root, text="Convert", command=convert_to_cm)
b1.place(x=20, y=100)

root.mainloop()
