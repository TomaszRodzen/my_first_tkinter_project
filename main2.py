import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print('Return key pressed.')


def log(event):
    print(event)


root = tk.Tk()

btn = ttk.Button(root, text='Save')
btn.bind('<Return>', return_pressed)
btn.bind('<Return>', log, add='+')

btn.focus()
btn.pack(expand=True)



def button_clicked():
    print('Button clicked')


button = ttk.Button(root, text='Click ME', command=button_clicked)
button.pack()


def select(option):
    print(option)


ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper', command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()

message = tk.Label(root, text="Hello, world!")
message.pack()

root.title('Tkinter window demo')



window_witdh = 500
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


center_x = int(screen_width/2 - window_witdh/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_witdh}x{window_height}+{center_x}+{center_y}')

root.minsize(400, 300)
root.maxsize(800,650)

root.attributes('-alpha', 0.95)

root.attributes('-topmost', 1)
root.iconbitmap('./images.ico')

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

ttk.Label(root, text='Hi there').pack()

label = ttk.Label(root)
label['text'] = 'Hi, there'
label.pack()

label = ttk.Label(root)
label.config(text='Hi, there')
label.pack()


root.mainloop()