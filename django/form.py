 #! C:/Users/lenovo/AppData/Local/Programs/Python/Python310/python.exe
#form .py
#!/usr/bin/env python
print("Content-Type: text/html")
print()

import cgi   
form= cgi.FieldStorage()

import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="formdjango",
      port="3306")

mycursor = mydb.cursor()


file = open('C:/xampp/htdocs/django/textform.txt',encoding="utf8")
file_content = file.read()
file.close()


query = "INSERT INTO textdata (text) VALUES (%s)"

mycursor.execute(query, (file_content,))


mydb.commit()
mycursor.close()
mydb.close()


