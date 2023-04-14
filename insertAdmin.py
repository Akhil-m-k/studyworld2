#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="", database="adminDetails")
cur = con.cursor()
padminId = "admin003"
ppassword = "admin@123"
q = """ insert into Admin(adminId,password)values('%s', '%s')"""%(padminId, ppassword)

cur.execute(q)
con.commit()
print("""
 <script>
 alert("data inserted  successfully...!");
 </script>
""")

con.close()