#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="", database="adminDetails")
cur = con.cursor()
import cgi
f= cgi.FieldStorage()
pid = f.getvalue("id")
q = """ Delete from stud WHERE id='%s' """%(pid)
cur.execute(q)
con.commit()
print("""
       <script>
           location.href="studExist.py"
           alert("successfully edited....!")
       </script>
   """)
con.close()