import mysql.connector

bd = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "marianokpo22"
)

print(bd)