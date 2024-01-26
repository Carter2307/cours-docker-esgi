import mysql.connector

mydb = mysql.connector.connect(
    host="db",
    user="root",
    password="",
    database="python-customers"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)