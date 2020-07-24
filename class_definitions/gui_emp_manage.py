# -*- coding: utf-8 -*-
"""
Created on 7/23/2020	
@author: Anthony Hamlin
Program: gui_emp_manage.py

This program provides the graphical user interface to manage
the employee database file csv_to_db_emp_manage.py which imports
a csv file and creates a SQLite3 database.
"""
import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import ttk
from tkinter import W
from tkinter import Menu
from class_definitions import csv_to_db_emp_manage as empdb


class DisplayEDMA:
    """
    Display DB CRUD Functions
    """
    def __init__(self):
        self.win = tk.Tk()
        # set the initial window size (width, height)
        # win.minsize(300, 250)
        self.win.attributes("-topmost", True)
        self.win.title("EDMA")
        app_label = ttk.Label(self.win, text="Employee Data Management", font=10)
        app_label.grid(row=0, sticky=tk.W, columnspan=8, padx=5, pady=5)
        self.tab_controls()

    def tab_controls(self):
        """
        START CONTROL TABS
        Tab are created and the content is nested in a 'LabelFrame'

        Create Tab Content
        """
        # Create Record tab control and creation
        tab_control = ttk.Notebook(self.win)  # control for tab
        create_tab = ttk.Frame(tab_control)  # create tab
        tab_control.add(create_tab, text="Create Record")  # add the tab
        # nest tab control in LabelFrame(s)
        # Nest Create Record Tab
        ctab_frame = ttk.LabelFrame(create_tab, text=" Create Functions ")
        ctab_frame.grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(ctab_frame, text="Create a Record").grid(row=0, sticky="W", column=0)

        """Read Tab Content"""
        # Read Record Tab
        read_tab = ttk.Frame(tab_control)  # create tab
        tab_control.add(read_tab, text="Read Record(s)")  # add the tab
        # Nest Read Record Tab
        rtab_frame = ttk.LabelFrame(read_tab, text=" Read Functions ")
        rtab_frame.grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(rtab_frame, text="Read a Record").grid(row=0, sticky="W", column=0)

        """Update Tab Content"""
        # Update Record Tab
        update_tab = ttk.Frame(tab_control)  # create tab
        tab_control.add(update_tab, text="Update Record(s)")  # add the tab
        # Nest Update Record Tab
        utab_frame = ttk.LabelFrame(update_tab, text=" Update Functions ")
        utab_frame.grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(utab_frame, text="Update a Record").grid(row=0, sticky="W", column=0)

        """Delete Tab Content"""
        # Delete Record Tab
        delete_tab = ttk.Frame(tab_control)  # create tab
        tab_control.add(delete_tab, text="Delete Record(s)")  # add the tab
        # Nest Delete Record Tab
        dtab_frame = ttk.LabelFrame(delete_tab, text=" Delete Functions ")
        dtab_frame.grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(dtab_frame, text="Delete a Record").grid(row=0, sticky="W", column=0)

        tab_control.grid()  # make tabs visible

        # menu bar actions
        def _quit():  # private function
            """
            Quit/Destroy Application GUI cleanly
            """
            self.win.quit()
            self.win.destroy()
            exit()

        # Top Menu bar
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)
        # File Menu Bar items
        file_menu = Menu(menu_bar, tearoff=0)
        # TODO: remove unused menu items
        file_menu.add_command(label="New")
        file_menu.add_command(label="Save Changes")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=_quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # help/about menu bar items
        about_menu = Menu(menu_bar, tearoff=0)
        about_menu.add_command(label="About")
        menu_bar.add_cascade(label="Help", menu=about_menu)

        self.win.mainloop()


if __name__ == '__main__':
    DisplayEDMA()
