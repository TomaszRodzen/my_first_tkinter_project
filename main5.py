import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


def button_clicked():
    print('button clicked')

def return_button(event):
    print('return button clicked')

root = tk.Tk()


label = ttk.Label(root, text='hello world')
label.pack()


root.title('tkinter demo')

window_width = 500
window_heigth = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_heigth/2)


root.geometry(f'{center_x}x{center_y}+{window_width}+{window_heigth}')
root.minsize(300, 200)
root.maxsize(800, 700)

root.attributes('-alpha', 0.95)
root.attributes('-topmost', 1)

root.iconbitmap('images.ico')


button = ttk.Button(root, text='click me', command=button_clicked)
button.pack()

btn = ttk.Button(root, text='Save')
btn.bind('<Return>', return_button)
btn.focus
btn.pack()

email = tk.StringVar()
password = tk.StringVar()

def login_clicked():
    msg = f'you eneterd email: {email.get()} and password: {password.get()}'
    showinfo(title='information', message=msg)


signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

email_label = ttk.Label(signin, text='email address:')
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

password_label = ttk.Label(signin, text='Password')
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password)
password_entry.pack(fill='x', expand=True)

login_button = ttk.Button(signin, text='Login', command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)




root.mainloop()
