# -*- coding: utf-8 -*-
"""
Created on 7/16/2020
@author: Anthony Hamlin
Program: dsp_three_view_selection.py

This program is a GUI interface to the person_student.db database file by
providing CRUD actions.
This window provides the ability to view records from the two tables in the db.
"""
import tkinter as tk
from tkinter import W
from crud_gui import create_db_with_tables as ps_db


class DisplayThree:
    """START Third WINDOW - View DB selection"""
    def __init__(self):
        self.m3 = tk.Tk()  # where m is the name of the main window object
        # focus window on top
        self.m3.attributes("-topmost", True)
        # window title
        self.m3.title('DB CRUD')

        def view_person():
            """
            wrap the execution so it can be passed to the method
            """
            view_rows = ''
            conn = ps_db.create_connection("person_student.db")
            with conn:
                rows = ps_db.select_all_persons(conn)
                # loop thru rows
                for row in rows:
                    view_rows += '#' + str(row[0]) \
                                 + ', ' + str(row[1]) \
                                 + ' ' + str(row[2]) + '\n'
                    # print(row)
                view_label = tk.Label(self.m3, text=view_rows)
                view_label.grid(row=1, padx=5, pady=2)

        def view_student():
            """
            wrap the execution so it can be passed to the method
            """
            view_rows = ''
            conn = ps_db.create_connection("person_student.db")
            with conn:
                rows = ps_db.select_all_students(conn)
                # loop thru rows
                for row in rows:
                    view_rows += '#' + str(row[0]) \
                                 + ', Major: ' + str(row[1]) \
                                 + ', Start Date: ' + str(row[2]) + '\n'
                    # print(row)
            view_label = tk.Label(self.m3, text=view_rows)
            view_label.grid(row=3, padx=5, pady=2)

        self.view_person_btn = tk.Button(self.m3,
                                         text='Click to View Person Data',
                                         width=45)
        self.view_person_btn['command'] = lambda: view_person()
        self.view_person_btn.grid(row=0, sticky=W, padx=5)

        self.view_person_btn = tk.Button(self.m3,
                                         text='Click to View Student Data',
                                         width=45)
        self.view_person_btn['command'] = lambda: view_student()
        self.view_person_btn.grid(row=2, sticky=W, padx=5)

        self.add_db_btn = tk.Button(self.m3, text='Exit',
                                    width=45, command=self.m3.destroy)
        self.add_db_btn.grid(row=4)
        self.m3.mainloop()  # infinite loop that waits for events to happen
        """END OF third WINDOW"""


if __name__ == '__main__':
    DisplayThree()
