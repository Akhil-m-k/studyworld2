#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root", password="", database="")
cur = conn.cursor()
q = """create database adminDetails"""
cur.execute(q)
conn.commit()
print("""
 <script>
   alert("database created successfully...!");
 </script>
""")

conn.close()