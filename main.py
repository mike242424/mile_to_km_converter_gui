import tkinter
from tkinter import *


def convert_miles_to_kilometers():
    user_input = miles_entry.get()
    kilo_answer_label['text'] = f'{round(float(user_input) * 1.609344, 2)} kilometers'


distance = 0

window = Tk()
window.title('Convert Miles To Kilometers')
window.minsize(500, 300)
window.config(padx=80, pady=60)

main_label = Label(text="Enter a value in miles:", font=("Arial", 16))
main_label.grid(column=1, row=0)
main_label.config(padx=0, pady=10)

miles_label = Label(text="Miles", font=("Arial", 16))
miles_label.grid(column=2, row=1)
miles_label.config(padx=0, pady=10)

miles_entry = tkinter.Entry(width=10)
miles_entry.grid(column=1, row=1)

kilo_label_one = Label(text='is equal to', font=("Arial", 16))
kilo_label_one.grid(column=0, row=2)
kilo_label_one.config(padx=0, pady=10)

kilo_answer_label = Label(text=distance, font=("Arial", 16))
kilo_answer_label.grid(column=1, row=2)

kilo_label_two = Label(text='Kilometers', font=("Arial", 16))
kilo_label_two.grid(column=2, row=2)

convert_button = Button(text='Convert', command=convert_miles_to_kilometers)
convert_button.grid(column=1, row=3)

window.mainloop()

