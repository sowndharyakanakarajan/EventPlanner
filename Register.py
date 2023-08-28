#!C:\python 311\python.exe

import cgi
import mysql.connector
print("Content-type:text/html\r\n\r\n")

print("<html>")
print("<body>")

form=cgi.FieldStorage()
fname=form.getvalue("name")
femail=form.getvalue("email")
fevents=form.getvalue("events")
faddress=form.getvalue("address")
fphone=form.getvalue("phone")

mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="event planner"
            )
mycursor=mydb.cursor()

sql="INSERT INTO USERS(Name,email,events,address,phone)VALUES(%s,%s,%s,%s,%s)";
val=(fname,femail,fevents,faddress,fphone)

mycursor.execute(sql,val)
mydb.commit()

print("<h1>",fname,femail,fevents,faddress,fphone,"</h1>")
print("</body>")
print("</html>")