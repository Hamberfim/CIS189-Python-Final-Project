# -*- coding: utf-8 -*-
"""
Created on 7/24/2020	
@author: Anthony Hamlin
Program: gui_tabs.py
Used to mock up and test gui look, feel, and positioning
"""
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
# set the initial window size (width, height)
# win.minsize(300, 250)
win.attributes("-topmost", True)
win.title("EDMA")

# tab control and creation
tab_control = ttk.Notebook(win)  # control for tab
create_tab = ttk.Frame(tab_control)  # create tab
tab_control.add(create_tab, text="Create Record")  # add the tab

read_tab = ttk.Frame(tab_control)  # create tab
tab_control.add(read_tab, text="Read Record(s)")  # add the tab

update_tab = ttk.Frame(tab_control)  # create tab
tab_control.add(update_tab, text="Update Record(s)")  # add the tab

delete_tab = ttk.Frame(tab_control)  # create tab
tab_control.add(delete_tab, text="Delete Record(s)")  # add the tab

tab_control.pack(expand=1, fill="both")  # pack to make visible

# nest tab control in LabelFrame(s)
ctab_frame = ttk.LabelFrame(create_tab, text=" Create Functions ")
ctab_frame.grid(row=0, column=0, padx=5, pady=5)
ttk.Label(ctab_frame, text="Create a Record").grid(row=0, sticky="W", column=0)

rtab_frame = ttk.LabelFrame(read_tab, text=" Read Functions ")
rtab_frame.grid(row=0, column=0, padx=5, pady=5)
ttk.Label(rtab_frame, text="Read a Record").grid(row=0, sticky="W", column=0)

utab_frame = ttk.LabelFrame(update_tab, text=" Update Functions ")
utab_frame.grid(row=0, column=0, padx=5, pady=5)
ttk.Label(utab_frame, text="Update a Record").grid(row=0, sticky="W", column=0)

dtab_frame = ttk.LabelFrame(delete_tab, text=" Delete Functions ")
dtab_frame.grid(row=0, column=0, padx=5, pady=5)
ttk.Label(dtab_frame, text="Delete a Record").grid(row=0, sticky="W", column=0)

win.mainloop()
