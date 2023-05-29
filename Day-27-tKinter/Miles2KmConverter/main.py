import tkinter as tk
from tkinter.ttk import Label, Button, Entry


def button_clicked():
    user_input = entry.get()
    output_km = round(float(user_input) * 1.60934, 2)
    output_label["text"] = output_km


root = tk.Tk()
root.title("Miles to Km Converter.")
root.minsize(height=200, width=300)
root.config(padx=25, pady=25)

label_1 = Label(root, text="is equal to", font=("Arial", 14))
label_1.grid(row=1, column=0)
label_1.config(padding=10)

entry = Entry(width=20)
entry.insert(0, "")
entry.grid(column=1, row=0)

output_label = Label(root, text="0", font=("Arial", 14))
output_label.grid(row=1, column=1)
output_label.config(padding=10)

button_calc = Button(text="Calculate", command=button_clicked)
button_calc.grid(column=1, row=3)

button = Button(text="New Button", command=button_clicked)
button.grid(column=2, row=0)

label_2 = Label(root, text="miles", font=("Arial", 14))
label_2.grid(row=0, column=2)
label_2.config(padding=10)

label_3 = Label(root, text="km", font=("Arial", 14))
label_3.grid(row=1, column=2)
label_3.config(padding=10)

root.mainloop()
