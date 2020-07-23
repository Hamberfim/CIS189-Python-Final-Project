"""Used to mock up and test gui look, feel, and positioning"""
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Employee Data Management")
ttk.Label(win, text="A Label").grid(row=0, column=0)
win.mainloop()
