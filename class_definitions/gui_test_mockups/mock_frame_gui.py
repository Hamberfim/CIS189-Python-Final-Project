"""
Created on 7/23/2020
@author: Anthony Hamlin
Program: mock_frame_gui.py
Used to mock up and test gui look, feel, and positioning
"""
import tkinter as tk
from tkinter import ttk
from tkinter import N
from tkinter import S
from tkinter import W
from tkinter import E
from tkinter import Menu
from tkinter import scrolledtext


win = tk.Tk()
win.title("EDMA")
win.attributes("-topmost", True)
# win.minsize(500, 300)
f_label = ttk.Label(win, text="Employee Data Management", font=10)
f_label.grid(row=0, sticky=tk.W, columnspan=8, padx=5, pady=5)

# Start of Column A(0)
frame_col_A = ttk.LabelFrame(win, text=' Column A')
frame_col_A.grid(row=1, sticky=tk.W, column=0, padx=5, pady=5)
ttk.Label(frame_col_A, text='Row=1 Col=0').grid(row=0, column=0)

# Start of Column B(1)
frame_col_B = ttk.LabelFrame(win, text=' Column B')
frame_col_B.grid(row=1, sticky=tk.W, column=1, padx=5, pady=5)
ttk.Label(frame_col_B, text='Row=1 Col=1').grid(row=0, column=0)

# Start of Column C(2)
frame_col_B = ttk.LabelFrame(win, text=' Column C')
frame_col_B.grid(row=1, sticky=tk.W, column=2, padx=5, pady=5)
ttk.Label(frame_col_B, text='Row=1 Col=2').grid(row=0, column=0)

# scroll text control wrap by word not char
row_two_fill_colms = ttk.LabelFrame(win, text='Message box')
row_two_fill_colms.grid(row=2, sticky='WE', columnspan=3,
                        padx=5, pady=5)
scrollW = 35
scrollH = 5
scroll = scrolledtext.ScrolledText(row_two_fill_colms, width=scrollW,
                                   height=scrollH,
                                   wrap=tk.WORD)
scroll.grid(row=2, sticky='WE', column=0, columnspan=3)


# menu bar actions
def _quit():  # private function
    """
    Quit/Destroy Application GUI cleanly
    """
    win.quit()
    win.destroy()
    exit()


# Top Menu bar
menu_bar = Menu(win)
win.config(menu=menu_bar)
# File Menu Bar items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Save Changes")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# help/about menu bar items
about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=about_menu)

win.mainloop()
