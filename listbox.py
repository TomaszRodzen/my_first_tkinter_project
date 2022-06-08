import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name


root = tk.Tk()
root.title('combox, listbox, paned window and slider demo')
root.geometry('300x200')
root.resizable(False, False)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

langs = ('Java', 'C#', 'C', 'C++', 'Python',
        'Go', 'JavaScript', 'PHP', 'Swift')

langs_var = tk.StringVar(value=langs)

#list_box_frame = ttk.Frame(root)
listbox = tk.Listbox(root, listvariable=langs_var, height=6, selectmode='extended')
listbox.grid(column=0, row=0, sticky='nwes')


def items_selected(event):
    selected_indices = listbox.curselection()
    selected_langs = ','.join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'
    showinfo(title='Information', message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)


root.mainloop()