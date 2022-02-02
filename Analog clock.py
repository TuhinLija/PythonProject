import tkinter as ui
import time


window = ui.Tk()

window.geometry("400×400")

def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm

canvas = ui.Canvas(window, width=400, height=400, bg="black")
canvas.pack(expand=True, fill='both')


bg = ui.PhotoImage(file='dial_400.png')
canvas.create_image(200, 200, image=bg)


update_clock()


window.mainloop()