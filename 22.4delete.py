#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","harsh","123","database1" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
var="DELETE FROM student WHERE Name='Rohit' AND Class='10'" 
# execute SQL query using execute() method.
cursor.execute(var)

var2="SELECT * FROM student"
cursor.execute(var2)

# Fetch a all rows using fetchall() method.
rows = cursor.fetchall()
for x in rows:
    print (x)

#connection is not autocommit by default. So you must commit to save your changes to the sql server
db.commit()

# disconnect from server
db.close()
