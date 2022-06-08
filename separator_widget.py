import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry('300x200')
root.resizable(False, False)

root.title('separator widget demo')

ttk.Label(root, text='first label').pack()

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x')
ttk.Label(root, text='second label').pack()

root.mainloop()