import tkinter
import turtle

window = tkinter.Tk()
window.title("My first GUU Program")
window.minsize(width=500, height=300)
my_label = tkinter.Label(text="I am a label", font =("Arial", 24,"Bold"))
my_label.pack(side="left")


tim = turtle.Turtle()
tim.write()

window.mainloop()