"""Used to mock up and test gui look, feel, and positioning"""
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.attributes("-topmost", True)
win.title("Employee Data Management")

# label to change on click
f_label = ttk.Label(win, text="first (Top) Label")
f_label.grid(row=0, columnspan=2)


def click_action():
    """
    handles button click actions to change label text
    """
    f_label.configure(text='Hello ' + name.get() + ' ' + chosen.get())


# input field
name = tk.StringVar()
name_entry = ttk.Entry(win, width=25, textvariable=name)
name_entry.grid(row=1, columnspan=2)
name_entry.focus()

# combo box selection label
comb_box = ttk.Label(win, text='Choose:')
comb_box.grid(row=2, column=0)
# combo box selection
choice = tk.StringVar()
chosen = ttk.Combobox(win, width=15, textvariable=choice, state='readonly')
# tuple of values to choose from
chosen['values'] = (', U goof!', ', Mr. Smarty', ', U Nerd', ', U poo poo face.')
chosen.grid(row=2, column=1)
chosen.current(0)

# button to call click_action to change label with textvariable/StringVar
action_btn = ttk.Button(win, text='Submit', command=click_action)
action_btn.grid(row=3, columnspan=2)

win.mainloop()
