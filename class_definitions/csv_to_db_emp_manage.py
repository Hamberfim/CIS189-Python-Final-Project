# -*- coding: utf-8 -*-
"""
Created on 7/21/2020	
@author: Anthony Hamlin
Program: csv_to_db_emp_manage.py

This program imports a csv file and creates a SQLite3 database
and then the database is managed through a tkinter GUI.

    Test if database already exists, if not:
        Run Script for Data Exchange:
            * Read the CSV file,
            * create a SQLite3 database with table,
            * use first row headers for column names,
            * populate the table with the data.
TODO:
        else:
            * make db connection
            * provide CRUD functionality
    Build GUI on top with CRUD functionality
"""
import os
import csv
import sqlite3
from sqlite3 import Error
from class_definitions import csv_to_sqlite

# name of the database to create
db_file_name = "employee.db"

# check if database exist in the working directory
db_is_new = not os.path.exists(db_file_name)
# check if db exists, if not create it from the csv file
if db_is_new:
    # csv-to-sqlite --help
    # SQLite type and encoding options
    opt = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250")
    # a list of CSV files separated by commas
    input_files = ["employees.csv"]
    # write the database
    csv_to_sqlite.write_csv(input_files, db_file_name, opt)
else:
    # console output
    print(db_file_name, "database already exists.")
