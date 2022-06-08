import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.resizable(False, False)
root.title('scroll bar widget')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

text = tk.Text(root, height=10)
text.grid(row=0, column=0, sticky='ew')

scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

text['yscrollcommand'] = scrollbar.set

root.mainloop()