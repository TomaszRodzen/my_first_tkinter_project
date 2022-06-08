import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name


root = tk.Tk()
root.title('combox, listbox, paned window and slider demo')
root.geometry('300x200')
root.resizable(False, False)

label = ttk. Label(text='Please select month:')
label.pack(fill='x', pady=5, padx=5)

selected_moth = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_moth)

month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

month_cb['state'] = 'readonly'

month_cb.pack(fill='x', padx=5, pady=5)


def month_changed(event):
    showinfo(title='result', message=f' you selected {selected_moth.get()}!')


month_cb.bind('<<ComboboxSelected>>', month_changed)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

langs = ('Java', 'C#', 'C', 'C++', 'Python',
        'Go', 'JavaScript', 'PHP', 'Swift')

langs_var = tk.StringVar(value=langs)

list_box_frame = ttk.Frame(root)
list_box_frame.pack(fill='x')

listbox = tk.Listbox(list_box_frame, listvariable=langs_var, height=6, selectmode='extended')
listbox.grid(column=0, row=0, sticky='nwes')


def items_selected(event):
    selected_indices = listbox.curselection()
    selected_langs = ','.join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'
    showinfo(title='Information', message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)


root.mainloop()
