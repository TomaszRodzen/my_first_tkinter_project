import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText


root = tk.Tk()
root.title('scrolled text, separator, checkbox and radio button widget demo')

st = ScrolledText(root, width=40, height=10)
st.pack()

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x')

agreement = tk.StringVar()


def message():
    showinfo(title='information', message=agreement.get())


check_button = ttk.Checkbutton(text='I agree',
                               variable=agreement,
                               onvalue='agree',
                               offvalue='disagree',
                               command=message)

check_button.pack(fill='x')

separator2 = ttk.Separator(root, orient='horizontal')
separator2.pack(fill='x')


def show_selected_size():
    showinfo(title='selected size', message=selected_size.get())


selected_size = tk.StringVar()
sizes = (('small', 's'),
         ('medium', 'm'),
         ('larg', 'l'),
         ('extra large', 'xl'),
         ('extra extra large', 'xxl'))

label = ttk.Label(root, text='select your size')
label.pack(fill='x')

for size in sizes:
    r = ttk.Radiobutton(root, text=size[0] , value=size[1], variable=selected_size)
    r.pack(fill='x')
button = ttk.Button(root, text='get selected size', command=show_selected_size)
button.pack(fill='x')

root.mainloop()
