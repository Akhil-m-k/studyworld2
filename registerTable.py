#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="", database="adminDetails")
cur = con.cursor()
q = """   CREATE TABLE register(id int(10) AUTO_INCREMENT PRIMARY KEY,
            fullName varchar(50),
            Email varchar(80),
            Mobile varchar(15),
            Course varchar(60)
);"""

cur.execute(q)
con.commit()
print("""
 <script>
 alert("table created successfully...!");
 </script>
""")

con.close()