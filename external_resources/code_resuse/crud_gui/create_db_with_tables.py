# -*- coding: utf-8 -*-
"""
Created on 7/14/2020	
@author: Anthony Hamlin
Program: create_db_with_tables.py

This program is used to hand the 'backend' tasks of the GUI.
"""
import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)


def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(database):
    """Connect to DB and Creates DB tables"""
    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY,
                                    major text NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text,
                                    FOREIGN KEY (id) REFERENCES person (id)
                                );"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_person_table)
        # create tasks table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))


def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object this is generating error
    cur.execute(sql, person)
    # returns the row id of the cursor object, the person id
    return cur.lastrowid


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO student(id, major, begin_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    # returns the row id of the cursor object, the student id
    return cur.lastrowid


def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()
    # return the rows
    return rows


def select_all_students(conn):
    """Query all rows of student table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()
    # return the rows
    return rows


if __name__ == '__main__':
    pass
    """OLD DRIVER CODE FOR INITIAL TESTING"""
    # create_connection("pythonsqlite.db")
    # create_tables("pythonsqlite.db")
    """conn = create_connection("pythonsqlite.db")
    with conn:
        person = ('Rob', 'Thomas')
        person_id = create_person(conn, person)

        student = (person_id, 'Songwriting', '2000-01-01')
        student_id = create_student(conn, student)"""
    # query person records
    """conn = create_connection("pythonsqlite.db")
    with conn:
        rows = select_all_persons(conn)
        for row in rows:
            print(row)"""
    # query student records
    """conn = create_connection("pythonsqlite.db")
    with conn:
        rows = select_all_students(conn)
        for row in rows:
            print(row)"""