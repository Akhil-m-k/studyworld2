#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="", database="adminDetails")
cur = con.cursor()
q = """   CREATE TABLE staff(id int(10) AUTO_INCREMENT PRIMARY KEY,
    staffName varchar(20),
    staffId varchar(10),
    Department varchar(50),
    dob varchar(10),
    doj varchar(10),
    email varchar(50),
    mobile varchar(15),
    password varchar(10),
    profile varchar(500)
);"""

cur.execute(q)
con.commit()
print("""
 <script>
 alert("table created successfully...!");
 </script>
""")

con.close()