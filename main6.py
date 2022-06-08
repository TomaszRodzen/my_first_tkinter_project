import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def button_clicked():
    print('button clicked')

def return_key_pressed(event):
    print('return key pressed')

root = tk.Tk()

label = ttk.Label(root, text='hello, world')
label.pack()

root.title('this is demo')

window_width = 400
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

centerx = int(screen_width/2 - window_width/2)
centery = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{centerx}+{centery}')
root.maxsize(700, 600)
root.minsize(200, 100)

root.attributes('-alpha', 0.95)
root.attributes('-topmost', 1)

root.iconbitmap('images.ico')

button = ttk.Button(root, text='click me', command=button_clicked)
button.pack()

btn = ttk.Button(root, text='save')
btn.bind('<Return>', return_key_pressed)
btn.pack()

email = tk.StringVar()
password = tk.StringVar()


def login_clicked():
    msg = f'you entered email: {email.get()} and password: {password.get()}'
    showinfo(title='information', message=msg)


signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, expand=True, fill='x')

email_label = ttk.Label(signin, text='email addres:')
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

password_label = ttk.Label(signin, text='password:')
password_label.pack(padx=10, pady=10, expand=True, fill='x')

password_entry = ttk.Entry(signin, textvariable=password, )
password_entry.pack(fill='x', expand=True)


button2 = ttk.Button(signin, text='login', command=login_clicked)
button2.pack(fill='x', expand=True, pady=10)







root.mainloop()
