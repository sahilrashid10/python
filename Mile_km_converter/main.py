from tkinter import *


def calculate():
    m = float(label1_input.get())
    km = round(m*1.60934)
    label3.config(text=f"{km:.2f}km")


window = Tk()
window.title("Miles-KM converter")
window.config(padx=100, pady=20)

label1_input = Entry(width=7)
label1_input.grid(column=4, row=3)

label2 = Label(text="miles")
label2.grid(column=5, row=3)

label3 = Label(text="0")
label3.grid(column=4, row=4)

label4 = Label(text="km")
label4.grid(column=5, row=4)

label5 = Label(text="is equal to ")
label5.grid(column=2, row=4)




button = Button(text="Calculate")
button.grid(column=4, row=6)
button.config(command=calculate)
window.mainloop()
