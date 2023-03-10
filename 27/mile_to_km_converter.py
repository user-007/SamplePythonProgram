from tkinter import *

def miles_to_lm():
    miles = miles.input_get()
    km = miles * 1.609
    kilometer_result_label.config(text=km)

window = Tk()
window.title("Miles to Kilometer Converter")

miles_input = Entry()
miles_input.grid(column=, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row = 0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row =2)
kilometer_result_label = Label(text="0")

kilometer_label = Label(text="km")

calculate_button = Button(text = "Calculate")
