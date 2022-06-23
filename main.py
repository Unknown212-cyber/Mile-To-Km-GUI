from tkinter import *


def convert():
    m = float(miles_input.get())
    result = round(m * 1.609)
    answer.config(text=f"{result}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

answer = Label(text='0', font=("Arial", 15, "normal"))
answer.grid(column=1, row=1)
miles = Label(text="Miles", font=("Arial", 15, "normal"))
miles.grid(column=2, row=0)
km = Label(text="Km", font=("Arial", 15, "normal"))
km.grid(column=2, row=1)
is_equal_to = Label(text="is equal to", font=("Arial",  15, "normal"))
is_equal_to.grid(column=0, row=1)

calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()
