import tkinter
from tkinter import *


def convert_miles_to_kilometers():
    user_input = my_input.get()
    answer_label['text'] = f'{round(float(user_input) * 1.609344, 2)} kilometers'


distance = 0

window = Tk()
window.title('Convert Mile To Kilometers')
window.minsize(500, 300)
window.config(padx=80, pady=30)

# Label
my_label = Label(text="Enter a value in miles:", font=("Arial", 16))
my_label.grid(column=1, row=0)
my_label.config(padx=0, pady=20)

# Label
miles_label = Label(text="Miles", font=("Arial", 16))
miles_label.grid(column=2, row=1)
miles_label.config(padx=0, pady=20)

# Entry
my_input = tkinter.Entry(width=20)
my_input.grid(column=1, row=1)

# Button
button = Button(text='Convert', command=convert_miles_to_kilometers)
button.grid(column=1, row=3)

# Label
label_text_one = Label(text='is equal to ', font=("Arial", 16))
label_text_one.grid(column=0, row=2)

# Label
answer_label = Label(text=distance, font=("Arial", 16))
answer_label.grid(column=1, row=2)
answer_label.config(padx=0, pady=10)

# Label
label_text_two = Label(text='Kilometers', font=("Arial", 16))
label_text_two.grid(column=2, row=2)

window.mainloop()

