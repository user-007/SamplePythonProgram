from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(pads=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=256)
card_front_img = PhotoImage(file='images/card/card_font.png')
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0)

window.mainloop()

