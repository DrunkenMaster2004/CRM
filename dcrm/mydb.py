import mysql.connector
dataBase = mysql.connector.connect(host='localhost', user='root', passwd='12345')
cursor = dataBase.cursor()
cursor.execute("CREATE DATABASE elderco")
print("All done!")