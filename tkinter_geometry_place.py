import tkinter as tk


root = tk.Tk()

root.title('tkinter place geometry mamanger')


label1 = tk.Label(root, text='absolute placement', bg='red', fg='white')

label1.place(x=20, y=10)

label1 = tk.Label(root, text='relative placement', bg='blue', fg='white')

label1.place(relx=0.8, rely=0.2 , relwidth=0.5, anchor='ne')

root.mainloop()