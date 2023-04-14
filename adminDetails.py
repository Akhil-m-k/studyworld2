#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="", database="adminDetails")
cur = con.cursor()
q = """   CREATE TABLE Admin(id int(10) AUTO_INCREMENT PRIMARY KEY,
    adminId varchar(20),
    password varchar(10)
);"""

cur.execute(q)
con.commit()
print("""
 <script>
 alert("table created successfully...!");
 </script>
""")

con.close()