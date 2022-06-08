import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print('Return key pressed.')

def log(event):
    print(event)

root = tk.Tk()
root.title('Tkinter Window demo')

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

label = ttk.Label(root)
label.config(text='Hi there')
label.pack()

window_width = 500
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

messge = tk.Label(root, text="Hello, World!")
messge.pack()
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.minsize(250, 150)
root.maxsize(800, 650)
root.attributes('-alpha', 0.95, '-topmost', 1)
root.iconbitmap('./images.ico')

def button_clicked():
    print('button clicked')

button = ttk.Button(root, text='click Me', command=button_clicked)
button.pack()

def select(option):
    print(option)

ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper', command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scossprs', command=lambda: select('Scissors')).pack()


btn = ttk.Button(root, text='Save')
btn.bind('<Return>', return_pressed)
btn.bind('<Return>', log, add='+')

btn.focus()
btn.pack(expand=True)

ttk.Entry(root, text='Entry', ).pack()
root.bind_class('Entry', '<Control-V>')

btn.unbind('<Return>')



root.mainloop()


