#!/usr/bin/python
from sys import argv
import sqlite3
import time
script, mem  = argv


conn = sqlite3.connect('test.db')

print "Opened database successfully"

cursor = conn.execute("SELECT * from DETAILS WHERE MEMBERID = '%s'"%(mem))
for row in cursor:
    print "ID = ", row[0]
    print "NAME = ", row[1]
    print "GROUP = " ,row[2]
    #print "ADDRESS = " ,row[3]

print "Operation done successfully"
conn.close()