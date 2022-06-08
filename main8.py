import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('tkinter demo')

label = ttk.Label

window_width = 400
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)


root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.maxsize(600, 500)
root.minsize(200, 100)
root.attributes('-alpha', 0.95)
root.attributes('-topmost', 1)
root.iconbitmap('images.ico')


def button_cliked():
    print('button clicked')


button = ttk.Button(root, text='click me', command=button_cliked)
button.pack()


def return_key_pressed(event):
    print('return key pressed')


btn = ttk.Button(root, text='save')
btn.bind('<Return>', return_key_pressed)
btn.pack()

email = tk.StringVar()
password = tk.StringVar()


def login_clicked():
    msg = f'you entered email: {email.get()} and password: {password.get()}'
    showinfo(title='information', message=msg)

signin = ttk.Frame(root)
signin.pack(fill='x', expand=True)

email_label = ttk.Label(signin, text='email address')
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.focus()
email_entry.pack(fill='x', expand=True)

password_label = ttk.Label(signin, text='password')
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password)
password_entry.pack(fill='x', expand=True)


button2 = ttk.Button(signin, text='Login', command=login_clicked)
button2.pack(fill='x', expand=True)


root.mainloop()
