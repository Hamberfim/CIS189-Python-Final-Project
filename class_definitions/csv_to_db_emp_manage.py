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
        else:
            * make db connection
            * provide CRUD functionality
TODO:
    Build GUI on top with CRUD functionality
"""
import os
# import csv
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
    # SQLite type and encoding options must match cvs file
    opt = csv_to_sqlite.CsvOptions(typing_style="full", encoding="utf8")
    # a list of CSV files separated by commas
    input_files = ["employees.csv"]
    # write the database
    csv_to_sqlite.write_csv(input_files, db_file_name, opt)
else:
    # console output
    print(db_file_name, "database already exists.")


def create_connection(db_file_name):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db_file_name)
        return conn
    except Error as err:
        print(err)


def create_employee(conn, employee):
    """Create a new person for table
    :param conn:
    :param employee:
    :return: employee id
    """
    sql = ''' INSERT INTO employees(emp_id, EmployeeName, JobTitle, TotalPay)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, employee)
    # returns the row id of the cursor object, the student id
    conn.commit()
    return cur.lastrowid


def select_all_employees(conn):
    """Query all rows of employee table
    :param conn: the connection object
    :return: all rows of employee table
    """
    cur = conn.cursor()
    cur.execute('''SELECT oid, * FROM employees''')
    rows = cur.fetchall()
    # return the rows
    return rows


def update_employee_name(conn, employee):
    """Update Employee name
    :param conn:
    :param employee:
    :return: employee id
    """
    sql = ''' UPDATE employees
              SET EmployeeName = ? 
              WHERE oid = ?'''
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()


def update_employee_pay(conn, employee):
    """Update Employee TotalPay
    :param conn:
    :param employee:
    :return: employee id
    """
    sql = ''' UPDATE employees
              SET TotalPay = ? 
              WHERE oid = ?'''
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()


def update_employee_title(conn, employee):
    """Update employee JobTitle
    :param conn:
    :param employee:
    :return: employee id
    """
    sql = ''' UPDATE employees
              SET JobTitle = ? 
              WHERE oid = ?'''
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()


def delete_employee(conn, oid):
    """Delete a employee by employee id
    :param conn: database connection
    :param id: id of the employee
    :return:
    """
    sql = '''DELETE FROM employees WHERE oid=?;'''
    cur = conn.cursor()
    cur.execute(sql, (oid,))
    conn.commit()


def column_names(conn):
    """
    Internal Testing - use to get table column names
    equivalent to INFORMATION_SCHEMA.COLUMNS
    """
    cur = conn.cursor()
    cur.execute('''SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name;''')
    rows = cur.fetchall()
    # return the rows
    return rows


if __name__ == '__main__':
    # TODO: remove after testing
    """
    # get all records
    results = select_all_employees(sqlite3.connect(db_file_name))
    for row in results:
        print(row)
    
    # create a new record
    conn = create_connection(db_file_name)
    with conn:
        # emp_id, EmployeeName, JobTitle, TotalPay
        employee = ('000-102', 'William Rouge', 'Editor', '30000.00')
        emp_editor = create_employee(conn, employee)
    
    # update pay
    conn = create_connection(db_file_name)
    with conn:
        # TotalPay, oid
        employee = (66000.00, 101)
        update_employee_pay(conn, employee)

        rows = select_all_employees(conn)
        for row in rows:
            print(row)
    
    # update job title
    conn = create_connection(db_file_name)
    with conn:
        # JobTitle, oid
        employee = ('Chief Editor', 101)
        update_employee_title(conn, employee)

        rows = select_all_employees(conn)
        for row in rows:
            print(row)
    
    # update name
    conn = create_connection(db_file_name)
    with conn:
        # EmployeeName, oid
        employee = ('Billy', 101)
        update_employee_name(conn, employee)

        rows = select_all_employees(conn)
        for row in rows:
            print(row)
    
    # delete record
    conn = create_connection(db_file_name)
    with conn:
        delete_employee(conn, 101)
        rows = select_all_employees(conn)
        for row in rows:
            print(row)
    
    # get the column names, equivalent to INFORMATION_SCHEMA.COLUMNS
    col_names = column_names(sqlite3.connect(db_file_name))
    for col in col_names:
        print(col)"""
    pass
