#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="", database="adminDetails")
cur = con.cursor()
q = """   CREATE TABLE studLeave(id int(10) AUTO_INCREMENT PRIMARY KEY,
    studName varchar(20),
    studId varchar(20),
    fromDate varchar(15),
    toDate varchar(15),
    totalLeave varchar(10),
    reason varchar(1000),
    status varchar(20)
);"""

cur.execute(q)
con.commit()
print("""
 <script>
 alert("table created successfully...!");
 </script>
""")

con.close()