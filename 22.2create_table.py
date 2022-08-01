#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","harsh","123","database1" )


#use a database





# prepare a cursor object using cursor() method
cursor = db.cursor()
var="CREATE TABLE student(Name VARCHAR(20) NOT NULL , Class VARCHAR(20) NOT NULL )"
# execute SQL query using execute() method.
cursor.execute(var) #Creeates a table student in database harsh
cursor.execute("SHOW TABLES")

# Fetch a all rows using fetchall() method.
rows = cursor.fetchall()    #It stores the output row wise
for x in rows:  #we use for loop to print all the rows
    print (x)

# disconnect from server
db.close()
