"""Used to mock up and test gui look, feel, and positioning"""
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Employee Data Management")

f_label = ttk.Label(win, text="first Label")
f_label.grid(row=0, column=0)


def click_action():
    """
    handles button click actions
    """
    action.configure(text='Hello ' + name.get())


name = tk.StringVar()
name_entry = ttk.Entry(win, width=15, textvariable=name)
name_entry.grid(row=1, column=0)

action = ttk.Button(win, text='Submit', command=click_action)
action.grid(row=1, column=1)

win.mainloop()
