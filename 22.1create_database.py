#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","harsh","123" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
var = "CREATE DATABASE database3"   #to create a new database with name database2 
# execute SQL query using execute() method.
cursor.execute(var)

# disconnect from server
db.close()
