"""Used to mock up and test gui look, feel, and positioning"""
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.attributes("-topmost", True)
win.title("Employee Data Management")

# label to change on click
f_label = ttk.Label(win, text="first (Top) Label")
f_label.grid(row=0, column=0)


def click_action():
    """
    handles button click actions to change label text
    """
    f_label.configure(text='Hello ' + name.get())


name = tk.StringVar()
name_entry = ttk.Entry(win, width=15, textvariable=name)
name_entry.grid(row=1, column=0)

# call click_action to change label with textvariable/StringVar
action_btn = ttk.Button(win, text='Submit', command=click_action)
action_btn.grid(row=1, column=1)

win.mainloop()
