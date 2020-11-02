from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Clock")
app_window.geometry("400x150")
app_window.resizable(0, 0)

#Label Design
text_font = ("Boulder", 68)
background = "#000000"
foreground = "#ffffff"
border_width = 25

#Combining the elements
label = Label(app_window, font=text_font, bg = background, fg = foreground, bd = border_width)
label.grid(row = 0, column = 1)

#defining the function
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text = time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()