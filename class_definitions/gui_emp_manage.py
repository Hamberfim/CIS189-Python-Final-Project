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
from msilib.schema import ListView
from sqlite3 import Error
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import W, E, N, S
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
        app_label = ttk.Label(self.win, text="Employee Data Management",
                              font=10)
        app_label.grid(row=0, sticky=tk.W, columnspan=8, padx=5, pady=5)
        # call tabs into layout
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
        ctab_frame = ttk.LabelFrame(create_tab, text=" Add New Employee ")
        ctab_frame.grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(ctab_frame, text=" ").grid(row=1, sticky="W", column=0)

        tk.Label(ctab_frame, text="Employee Name:  ").grid(row=2, sticky=W,
                                                           padx=5, pady=2)
        ename = tk.Entry(ctab_frame, width=20)
        ename.grid(row=2)

        tk.Label(ctab_frame, text="Job Title:  ").grid(row=3, sticky=W, padx=5,
                                                       pady=2)
        etitle = tk.Entry(ctab_frame, width=20)
        etitle.grid(row=3)

        tk.Label(ctab_frame, text="Total Pay:  ").grid(row=4, sticky=W, padx=5,
                                                       pady=2)
        epay = tk.Entry(ctab_frame, width=20)
        epay.grid(row=4)
        self.new_emp_record_btn = tk.Button(ctab_frame, text='Add Employee',
                                            width=45)

        def clear_fields():
            """clear test fields after adding a person"""
            ename.delete(0, tk.END)
            etitle.delete(0, tk.END)
            epay.delete(0, tk.END)

        def new_emp_record(ename, etitle, epay):
            """
            wrap the execution so it can be passed to the method
            """
            employee_name = ename.get()
            job_title = etitle.get()
            total_pay = epay.get()
            conn = empdb.create_connection(empdb.db_file_name)
            with conn:
                # EmployeeName, JobTitle, TotalPay
                employee = (str(employee_name), str(job_title), str(total_pay))
                emp_edit = empdb.create_employee(conn, employee)

            # call to clear fields for new entry
            clear_fields()

        self.new_emp_record_btn['command'] = lambda: new_emp_record(ename,
                                                                    etitle,
                                                                    epay)
        self.new_emp_record_btn.grid(row=5, sticky=W, padx=5, pady=5)
        """END CREATE RECORD TAB"""

        """Start Read Tab Content"""
        # Read Record Tab
        read_tab = ttk.Frame(tab_control)  # create tab
        tab_control.add(read_tab, text="Read Record(s)")  # add the tab
        # Nest Read Record Tab
        rtab_frame = ttk.LabelFrame(read_tab, text=" View Employees ")
        rtab_frame.grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(rtab_frame, text=" Mouse Scrolling ").grid(row=1,
                                                             sticky='WE',
                                                             column=0)

        def view_employees():
            """
            wrap the execution so it can be passed to the method
            """
            listbox = Listbox(rtab_frame, width=75)
            view_rows = ''
            conn = empdb.create_connection(empdb.db_file_name)
            with conn:
                rows = empdb.select_all_employees(conn)
                # loop thru rows
                for row in rows:
                    listbox.insert(END, '# ' + str(row[0]) + ',  '
                                   + str(row[1]) + ',  '
                                   + str(row[2]) + ',  '
                                   + str(row[3]) + '\n')

                view_label = ttk.Label(rtab_frame, text=view_rows)
                view_label.grid(row=2, padx=5, pady=2)

                scrollbar = Scrollbar(rtab_frame)
                # scrollbar.grid(row=3)
                listbox.grid(row=3, sticky='WE')
                listbox.config(yscrollcommand=scrollbar.set)
                scrollbar.config(command=listbox.yview)

        view_employees_btn = tk.Button(rtab_frame, text='View Employees',
                                       width=45)
        view_employees_btn['command'] = lambda: view_employees()
        view_employees_btn.grid(row=4, sticky=W, padx=5)
        """END READ RECORDS TAB"""

        """Update Tab Content"""
        # Update Record Tab
        update_tab = ttk.Frame(tab_control)  # create tab
        tab_control.add(update_tab, text="Update Record(s)")  # add the tab
        # Nest Update Record Tab
        utab_frame = ttk.LabelFrame(update_tab, text=" Update Functions ")
        utab_frame.grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(utab_frame, text="Update a Record").grid(row=0, sticky="W",
                                                           column=0)

        """Delete Tab Content"""
        # Delete Record Tab
        delete_tab = ttk.Frame(tab_control)  # create tab
        tab_control.add(delete_tab, text="Delete Record(s)")  # add the tab
        # Nest Delete Record Tab
        dtab_frame = ttk.LabelFrame(delete_tab, text=" Delete Functions ")
        dtab_frame.grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(dtab_frame, text="Delete a Record").grid(row=0, sticky="W",
                                                           column=0)

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
        file_menu.add_command(label="Exit", command=_quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # help/about menu bar items
        about_menu = Menu(menu_bar, tearoff=0)
        about_menu.add_command(label="About")
        menu_bar.add_cascade(label="Help", menu=about_menu)

        self.win.mainloop()


if __name__ == '__main__':
    DisplayEDMA()
