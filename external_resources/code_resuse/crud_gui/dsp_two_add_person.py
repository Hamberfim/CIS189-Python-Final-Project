# -*- coding: utf-8 -*-
"""
Created on 7/15/2020
@author: Anthony Hamlin
Program: dsp_two_add_person.py

This program is a GUI interface to the person_student.db database file by
providing CRUD actions.
This window provides the ability to add a person to the two tables in the db.
"""
import tkinter as tk
from tkinter import W
from external_resources.code_resuse.crud_gui import create_db_with_tables as ps_db
from external_resources.code_resuse.crud_gui import dsp_three_view_selection as dsp3


class DisplayTwo:
    """START SECOND WINDOW - Add Person"""
    def __init__(self):
        self.m2 = tk.Tk()  # where m is the name of the main window object
        # focus window on top
        self.m2.attributes("-topmost", True)
        # window title
        self.m2.title('DB CRUD')
        # labels and fields capture
        tk.Label(self.m2, text="First Name:  ").grid(row=0, sticky=W, padx=5,
                                                     pady=2)
        self.f_name = tk.Entry(self.m2, width=20)
        self.f_name.grid(row=0)

        tk.Label(self.m2, text="Last Name:  ").grid(row=1, sticky=W, padx=5,
                                                    pady=2)
        self.l_name = tk.Entry(self.m2, width=20)
        self.l_name.grid(row=1)

        tk.Label(self.m2, text="Major:  ").grid(row=2, sticky=W, padx=5,
                                                pady=2)
        self.major = tk.Entry(self.m2, width=20)
        self.major.grid(row=2)

        tk.Label(self.m2, text="Start Date:  ").grid(row=3, sticky=W, padx=5,
                                                     pady=2)
        self.s_date = tk.Entry(self.m2, width=20)
        self.s_date.grid(row=3)

        self.add_person_btn = tk.Button(self.m2, text='Click to Add Person',
                                        width=45)

        def clear_fields():
            """clear test fields after adding a person"""
            self.f_name.delete(0, tk.END)
            self.l_name.delete(0, tk.END)
            self.major.delete(0, tk.END)
            self.s_date.delete(0, tk.END)

        def add_person(f_name, l_name, major, s_date):
            """
            wrap the execution so it can be passed to the method
            """
            # retrieve the text and assign it
            first_name = f_name.get()
            last_name = l_name.get()
            major = major.get()
            s_date = s_date.get()
            conn = ps_db.create_connection("person_student.db")
            with conn:
                person = (str(first_name), str(last_name))
                person_id = ps_db.create_person(conn, person)
                student = (person_id, str(major), str(s_date))
                student_id = ps_db.create_student(conn, student)
            # call to clear fields for new entry
            clear_fields()

        self.add_person_btn['command'] = lambda: add_person(self.f_name,
                                                            self.l_name,
                                                            self.major,
                                                            self.s_date)
        self.add_person_btn.grid(row=4, sticky=W, padx=5)

        self.add_db_btn = tk.Button(self.m2, text='View Records',
                                    width=45, command=self.m2.destroy)
        self.add_db_btn.grid(row=5)
        self.m2.mainloop()  # infinite loop that waits for events to happen
        # call next display
        dsp3.DisplayThree()
        """END OF SECOND WINDOW"""


if __name__ == '__main__':
    DisplayTwo()
