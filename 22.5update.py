#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","harsh","123","database1" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
var="UPDATE student SET Class='6' WHERE Name='Adarsh'" 
# execute SQL query using execute() method.
cursor.execute(var)

db.rollback()   #to undo last changes

var2="SELECT * FROM student"
cursor.execute(var2)

rows = cursor.fetchall()
for x in rows:
    print (x)

# disconnect from server
db.close()
