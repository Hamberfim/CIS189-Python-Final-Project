"""
Created on 7/23/2020
@author: Anthony Hamlin
Program: mock_frame_gui.py
Used to mock up and test gui look, feel, and positioning
"""
import tkinter as tk
from tkinter import ttk


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

win.mainloop()
