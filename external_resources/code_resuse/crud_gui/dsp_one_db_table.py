# -*- coding: utf-8 -*-
"""
Created on 7/15/2020
@author: Anthony Hamlin
Program: dsp_one_db_table.py

This program is a GUI interface to the person_student.db database file by
providing CRUD actions.
This window provides the creation of the DB and the tables.
THIS IS THE STARTER FILE - LAUNCH THIS FIRST
"""
import tkinter as tk
from tkinter import W
from external_resources.code_resuse.crud_gui import create_db_with_tables as ps_db
from external_resources.code_resuse.crud_gui import dsp_two_add_person as dsp2


class DisplayOne:
    """START FIRST WINDOW - DB and Table creation"""
    def __init__(self):
        self.m = tk.Tk()  # where m is the name of the main window object
        # window title
        self.m.title('DB CRUD')

        # creation of db
        self.create_btn = tk.Button(self.m, text='Click to Create Database',
                                    width=45)
        # with the lambda expression
        self.create_btn['command'] = lambda: \
            ps_db.create_connection('person_student.db')
        self.create_btn.grid(row=0, sticky=W, padx=5)

        # creation of tables in db
        self.create_tables_btn = tk.Button(self.m,
                                           text='Click to Create Tables',
                                           width=45)
        self.create_tables_btn['command'] = lambda: ps_db.create_tables(
            'person_student.db')
        self.create_tables_btn.grid(row=1, sticky=W, padx=5)
        self.ex_db_btn = tk.Button(self.m,
                                   text='Click for Next Step',
                                   width=45, command=self.m.destroy)
        self.ex_db_btn.grid(row=2)
        self.m.mainloop()  # infinite loop that waits for events to happen
        # call next display
        dsp2.DisplayTwo()
        """END OF FIRST WINDOW"""


if __name__ == '__main__':
    DisplayOne()
