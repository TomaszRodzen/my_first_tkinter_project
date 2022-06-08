from tkinter import Tk, Text

root = Tk()

root.resizable(False, False)
root.title('text widget example')

text = Text(root, height=8)
text.insert('4.4', 'this is a text widget demo')
text.pack()

text['state'] = 'disabled'


root.mainloop()
