import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
root.title('scrolled text, separator, checkbox and radio button widget demo')

st = ScrolledText(root, width=40, height=10)
st.pack()

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=5)

agreement = tk.StringVar()


def message():
    tk.messagebox.showinfo(title='selected size', message=agreement.get())


check_button = ttk.Checkbutton(root,
                               text='I agree',
                               variable=agreement,
                               onvalue='agree',
                               offvalue='disagree',
                               command=message
                               )
check_button.pack(fill='x', expand=True, pady=5)

separator2 = ttk.Separator(root, orient='horizontal')
separator2.pack(fill='x', pady=5, expand=True)


def show_selected_size():
    showinfo(title='information', message=selected_size.get())


selected_size = tk.StringVar()
sizes = (('small', 's'),
         ('medium', 'm'),
         ('larg', 'l'),
         ('extra large', 'xl'),
         ('extra extra large', 'xxl'))

label = ttk.Label(root, text='select your size')
label.pack(fill='x', pady=5, expand=True)

for size in sizes:
    r = ttk.Radiobutton(root, text=size[0], value=size[1], variable=selected_size)
    r.pack(fill='x', pady=5)

button = ttk.Button(root, text='get selected size', command=show_selected_size)
button.pack(fill='x', pady=5, expand=True)

root.mainloop()
