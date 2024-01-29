from tkinter import *

def brl_to_euro():
    brl_amount = int(input.get())
    euro_value = brl_amount / 5.5
    result["text"] = "{:.2f}".format(euro_value)

window = Tk()
window.title("BRL to EURO Converter")
window.config(padx=20, pady=20)

# Labels
brl_label = Label(text="BRL")
brl_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

eur_label = Label(text="EUROS")
eur_label.grid(column=2, row=1)

# Entry
input = Entry(width=8)
input.grid(column=1, row=0)

# Result
result = Label(text="")
result.grid(column=1, row=1)

# Button
button = Button(text="Click Me", command=brl_to_euro)
button.grid(column=1, row=2)

window.mainloop()