import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('open sans', 62, 'bold' ), background='blue', foreground='white')
label.pack(anchor = 'center') 


def time():
    str = strftime("%H: %M: %S \n %D")
    label.config(text=str)
    label.after(1000,time)


time()
root.mainloop()