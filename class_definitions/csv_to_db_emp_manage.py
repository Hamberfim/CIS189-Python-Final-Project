# -*- coding: utf-8 -*-
"""
Created on 7/21/2020	
@author: Anthony Hamlin
Program: csv_to_db_emp_manage.py

This program imports a csv file and creates a SQLite3 database
and then the database is managed through a tkinter GUI.
TODO:
    Test if database already exists, if not:
        Run Script for Data Exchange:
            * Read the CSV file,
            * create a SQLite3 database with table,
            * use first row headers for column names,
            * populate the table with the data.
        else:
            * make db connection
            * provide CRUD functionality
    Build GUI on top with CRUD functionality
"""
import csv
import sqlite3
from sqlite3 import Error
from class_definitions import csv_to_sqlite

options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250")
input_files = ["employees.csv"]  # a list of CSV files separated by commas
csv_to_sqlite.write_csv(input_files, "employee.db", options)
