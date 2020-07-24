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

tab_control = ttk.Notebook(win)  # control for tab
tab1 = ttk.Frame(tab_control)  # create tab
tab_control.add(tab1, text="CRUD")
tab_control.pack(expand=1, fill="both")  # pack to make visable

win.mainloop()
