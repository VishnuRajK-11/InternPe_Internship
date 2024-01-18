import time
import tkinter as tk
import random

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    label.config(text=current_time ,foreground=f"#{random.randint(0, 0xFFFFFF):06x}")
    root.after(1000, update_time)

root = tk.Tk()
root.title("Clock")

label = tk.Label(root, font=("ds-digital",80), background='black')
label.pack(anchor='center')

update_time()

root.mainloop()