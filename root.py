#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE DETAILS
    (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
    MEMBERID       CHAR(10)    NOT NULL,
    NAME            TEXT     NOT NULL,
    GROUPR           TEXT     NOT NULL,
    ADDRESS        CHAR(50),
    DESG TEXT, 
    DEPT TEXT);''')
print "Table created successfully";

conn.close()