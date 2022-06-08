import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo


root = tk.Tk()
root.title('scrolled text, separator, checkbox and radio button widget demo')

st = ScrolledText(root, width=40, height=10)
st.pack(pady=10)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=10)

agreement = tk.StringVar()


def agreement_changed():
    tk.messagebox.showinfo(title='result', message=agreement.get())


check_button = ttk.Checkbutton(root,
                               text='i agree',
                               command=agreement_changed,
                               variable=agreement,
                               onvalue='agree',
                               offvalue='disagree')
check_button.pack(fill='x', pady=10)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=10)


def show_selected_size():
    showinfo(title='Result', message=selected_size.get())


selected_size = tk.StringVar()
sizes = (('small', 's'),
         ('medium', 'm'),
         ('larg', 'l'),
         ('extra large', 'xl'),
         ('extra extra large', 'xxl'))

label = ttk.Label(text='whats your t-shir size?')
label.pack(fill='x', padx=5, pady=5)

for size in sizes:
    r = ttk.Radiobutton(root, text=size[0], value=size[1], variable=selected_size)
    r.pack(fill='x', padx=5, pady=5)

button = ttk.Button(root, text='get selected size', command=show_selected_size)
button.pack(fill='x', pady=5, padx=5)


root.mainloop()
