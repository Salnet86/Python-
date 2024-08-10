pip install pyodbc

 import pyodbc

 connessione al drive sql server Microsoft 

 cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for SQL 

Server};Server=myserver;Database=mydatabase;Port=myport;User 

ID=myuserid;Password=mypassword')

inserimenti record sql server 

cursor = cnxn.cursor() 

cursor.execute("INSERT INTO Cisco () VALUES () 

import pandas as pd

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ = 

test_db.mdb;')

cursor = conn.cursor()

consulta = '''

 SELECT COL_NAME1, COL_NAME2, COL_NAME3, COL_NAME4

 FROM TABLENAME1

 WHERE ID = & PROCESS = "" & CATEGORY IN ('', '', '')

 '''

df = pd.read_sql(consulta, conn)

conn = pypyodbc.connect("DRIVER={SQL Server};"

 "SERVER=server;"

"DATABASE=database;"

"Trusted_Connection=yes;")

cursor = conn.cursor()

cursor.execute('SELECT * FROM [table]')

for row in cursor:

 print('row = %r' % (row))
#-------------------------
import pyodbc
cnxn = pyodbc.connect(DRIVER='{SQL 
Server}',SERVER=SQLSRV01,DATABASE=DATABASE,UID=USER,PWD=PASSWORD)
cursor = cnxn.cursor()
cursor.execute("query sql server")
for row in cursor.fetchall():
 print row

 
programmazione python mysql 
import mysql.connector
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="*********",
password="******",
database="********"
)
mycursor = mydb.cursor()
sql = "INSERT INTO nome_tabella (,,,) VALUES (%s, %s,%s)"
val = (" ", " ",””)
ycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
#-------------------

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount,"Insert reord.")
mycursor =mydb.cursor()
mycursor.execute("SELECT * FROM nome_table")
myresult = mycursor.fetchall()
for x in myresult: 
 print(x)
impor mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
user="*********",
 password="******",
database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT item_1,item_2 FROM nome_tablella")
myresult = mycursor.fetchall()
for x in myresult:
 print(x)
#--------------

mycursor = mydb.cursor()
sql ="SELECT * FROM cisco WHERE address = %ip_anddress"
adr = ("Nova_cisco")
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
 print(x)
 
