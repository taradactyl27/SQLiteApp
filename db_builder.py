import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

dictTable1 = csv.DictReader(open("courses.csv")) #creates dict for cources.csv

dictTable2 = csv.DictReader(open("peeps.csv")) #creates dict for peeps.csv


command = "CREATE TABLE courses ('code' TEXT, 'mark' INTEGER, 'id' INTEGER);"          #SQL statement - creates table courses
c.execute(command)    #runs SQL statement

command = "CREATE TABLE peeps ('name' TEXT, 'age' INTEGER, 'id' INTEGER);"          #SQL statement - creates table courses
c.execute(command)    #runs SQL statement
for row in dictTable1:
    command = "INSERT INTO courses VALUES (" + "'" + row['code'] + "'" + ", " + row['mark'] + ", " + row['id'] + ");"  #SQL statement - populates the courses table
    c.execute(command)
    
for row in dictTable2:
    command = "INSERT INTO peeps VALUES (" + "'" + row['name'] + "'" + ", " + row['age'] + ", " + row['id'] + ");" # SQL statement - populates the peeps table
    c.execute(command)

db.commit() #save changes
db.close()  #close database
