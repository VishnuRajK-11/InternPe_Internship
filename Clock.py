import time
import tkinter as tk

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Clock")

label = tk.Label(root, font=("ds-digital",80), background='black', foreground='cyan')
label.pack(anchor='center')

update_time()

root.mainloop()