import tkinter as tk
from tkinter import ttk, Label
from tkinter.messagebox import showinfo

def pressed_button():
    print('button was pressed')

def return_pressed(event):
    print('return key pressed')

root = tk.Tk()
root.title('tkinter demo')

ttk.Label(root, text='themed label').pack()

button = ttk.Button(root, text='click me', command=pressed_button)
button.pack()

message = tk.Label(root, text='Hello, World!')
message.pack()

btn = ttk.Button(root, text='save')
btn.bind('<Return>', return_pressed)

btn.focus()
btn.pack(expand=True)

window_width = 300
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.minsize(200, 100)
root.maxsize(700, 600)

root.attributes('-alpha', 0.95)
root.attributes('-topmost', 1)
root.iconbitmap('images.ico')

label = Label(root, text='this is label')
label.pack(ipadx=10, ipady=10)


def callback():
    print('button clicked')


button2 = ttk.Button(root, text='demo button', command=callback)

button2.pack()
button2.state(['disabled'])

exit_button = ttk.Button(root, text='EXIT', command=lambda: root.quit())
exit_button.pack(ipadx=5, ipady=5, expand=True)

def download_clicked():
    showinfo(title='Information', message='Download button clicked!')


download_icon = tk.PhotoImage(file='./download.png')
download_button = ttk.Button(root,
                             image=download_icon,
                             text='Download', compound=tk.LEFT,
                             command=download_clicked)

download_button.pack(ipadx=5, ipady=5, expand=True)

text = tk.StringVar()
textbox = ttk.Entry(root, textvariable=text)
textbox.focus()
textbox.pack()


email = tk.StringVar()
password = tk.StringVar()


def login_clicked():
    msg = f'You entered email: {email.get()} and password: {password.get()}'
    showinfo(title='information', message=msg)


signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

email_label = ttk.Label(signin, text='Email address:')
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

password_label = ttk.Label(signin,text='Password:')
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show='*')
password_entry.pack(fill='x', expand=True)

login_button = ttk.Button(signin, text='Login', command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()