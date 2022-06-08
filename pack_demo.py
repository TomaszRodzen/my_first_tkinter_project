import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('250x150')

button1 = ttk.Button(text="Left")
button1.pack(side = tk.LEFT)

button2 = ttk.Button(text="Top")
button2.pack(side = tk.TOP)

button3 = ttk.Button(text="Right")
button3.pack(side = tk.RIGHT)

button4 = ttk.Button(text="Bottom")
button4.pack(side = tk.BOTTOM)

root.mainloop()