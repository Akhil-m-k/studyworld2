#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="", database="adminDetails")
cur = con.cursor()
import cgi
f= cgi.FieldStorage()
pid = f.getvalue("id")
q = """ UPDATE studLeave SET status='%s' WHERE id='%s' """%("Rejected",pid)
cur.execute(q)
con.commit()
print("""
       <script>
           location.href="newLeaveStud.py"
           alert("rejected....!")
       </script>
   """)
con.close()