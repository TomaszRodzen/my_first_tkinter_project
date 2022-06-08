import tkinter as tk
from tkinter import ttk

def pressed_button():
    print('button pressed')

def return_pressed(event):
    print('return key pressed')

root = tk.Tk()

message = tk.Label(root, text='Hello, world!')
message.pack()


root.title('tkinter demo')

ttk.Label(root, text='themed label').pack()

button = ttk.Button(root, text='click me', command=pressed_button)
button.pack()

btn = ttk.Button(root, text='save')
btn.bind('<Return>', return_pressed)
btn.focus
btn.pack()

window_height = 400
window_width = 500

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.minsize(300,200)
root.maxsize(700,600)

root.attributes('-alpha', 0.95)
root.attributes('-topmost', 1)
root.iconbitmap('images.ico')

root.mainloop()