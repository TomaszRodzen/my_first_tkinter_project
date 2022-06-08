import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.geometry('300x200')
root.title('Checkbox demo')
root.resizable(False, False)

agreement = tk.StringVar()


def agreement_changed():
    tk.messagebox.showinfo(title='Result', message=agreement.get())


ttk.Checkbutton(root, text='I agree', command=agreement_changed,
                variable=agreement, onvalue='agree', offvalue='disagree').pack()


root.mainloop()