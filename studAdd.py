#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="adminDetails")
cur = con.cursor()
q = """ select max(id) from stud"""
cur.execute(q)
r = cur.fetchone()
if r[0] != None:
    n = r[0]
else:
    n = 0
if n <= 9:
    z = "000"
elif n >= 10 and n <= 99:
    z = "00"
elif n >= 100 and n <= 999:
    z = "0"
studid = "stud" + z + str(n + 1)

print("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Study World College of Engineering,SWCE|</title>
    <link rel="icon" href="https://rdawvgw5kcwy.cdn.shift8web.com/wp-content/uploads/2022/09/favicon.png">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="utility.css">
    <link rel="stylesheet" href="staff.css">
    <link rel="stylesheet" href="width.css">
    <link rel="stylesheet" href="select.css">
    <style>
         .logout{
               display: none;
               top:50px;
               left:-48px;
               position: absolute;
               background-color:#ffff;
               min-width: 120px;
               z-index: 1;
               background-color:rgba(0,0,0);
               border-radius:15px;
           }
           .logout a{
              color: #ffff;
              padding: 12px 16px;
              text-decoration: none;
              display: block;
              white-space:nowrap;
           }
            li:last-child:hover .logout{
               display:block;
            }
            .logout .arrow{
                content:"";
                width:17px;
                height:17px;
                position:absolute;
                top:-7px;
                left:60px;
                 background-color:rgba(0,0,0);
                transform: rotate(45deg);
            }
    </style>

</head>
<body style="height:auto;">
    <!-- head-section -->
    <header>
        <div class="container-fluid ">

                <div class="container gap-xl-0 gap-3  top-section d-flex justify-content-center justify-content-xl-between align-items-center">
                    <div class="contact d-flex align-items-center">
                        <span><i class="fa-solid text-white fa-phone-flip"></i>&nbsp; &nbsp;  +91 99449 11933</span>
                        <span><i class="fa-solid fa-envelope text-white"></i> &nbsp; &nbsp;coimbatore@swehg.com</span>
                        <span><i class="fa-sharp fa-solid fa-location-dot text-white"></i>&nbsp; &nbsp; Alagu Nachiamman Kovil Road, Madukkarai.</span>
                    </div>
                     <div class="icons mb-3 mb-xl-0">
                        <span><a href="https://twitter.com/StudyWorldcbe"><i class="fa-brands fa-twitter text-secondary fa-xl"></i></a></span>
                        <span><a href="https://www.facebook.com/studyworldeng/"><i class="fa-brands fa-facebook text-secondary fa-xl"></i></a></span>
                        <span><a href="https://www.instagram.com/studyworldeng/?hl=en"><i class="fa-brands fa-instagram text-secondary fa-xl"></i></a></span>
                        <span><a href="https://www.youtube.com/channel/UCbMkk05LuXRiq8AihxMTICQ"><i class="fa-brands fa-youtube text-secondary fa-xl"></i></a></span>
                        <span><a href="https://www.linkedin.com/in/swce/?originalSubdomain=in"><i class="fa-brands fa-linkedin text-secondary fa-xl"></i></a></span>
                    </div>
                </div>

        </div>
    </header>

    <section class="navigation">

        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-lg container-fluid">
              <a class="navbar-brand" href="#"><img src="logo-swce (1).png " class="img-fluid"  alt=""></a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarNavDropdown">
                <ul class="navbar-nav ms-auto">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="index.py">Home</a>
                  </li>
                  <li class="nav-item ">
                   <div class="dropdown">
                      <button class="dropbtn" style="white-space: nowrap;">About Us
                        <i class="fa-solid fa-caret-down icon-1"></i>
                        <i class="fa-sharp fa-solid fa-caret-up icon-2" ></i>
                      </button>
                      <div class="dropdown-content" style="z-index:200;">
                        <a href="group.py">The Group</a>
                        <a href="AboutUs.py">Study world Educational Trust</a>
                        <a href="promoters.py">Promoters</a>
                        <a href="principal.py">Principal</a>
                      </div>
                    </div>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="courses.py">Courses</a>
                  </li>
                  
                 <li>
                    <div class="dropdown">
                          <button class="dropbtn">student
                            <i class="fa-solid fa-caret-down icon-1"></i>
                            <i class="fa-sharp fa-solid fa-caret-up icon-2" ></i>
                          </button>
                          <div class="dropdown-content" >
                            <a href="studAdd.py">New</a>
                            <a href="studExist.py">Existing</a>
                         </div>
                    </div>
                 </li>
                 
                  <li class="nav-item"> <a href="ContactUs.py" class="nav-link">Contact us</a></li>
                  
                  <li style=" padding-top:8px; padding-left:40px;">
                      <div class="dropdown">
                           <a onclick="logout(); return false;" style="text-align:center; "><i  class="fa-solid fa-2x fa-right-from-bracket"></i></a>                    
                          <div class="logout"  border-radius:10px;">
                            <div class="arrow"></div>
                            <a href="">Back to dashboard</a>
                          </div>
                     </div>

                  </li>
                </ul>
              </div>
            </div>
          </nav>
    </section>
    <section class="login pb-5 pt-5" style="height:auto;">
        <div class="container">
            <div class="row">
                <div class="col-12 d-flex justify-content-center">
                    <form action="" method="post"enctype="multipart/form-data">
                        <h1 style="margin-bottom:10px;">Sign-Up</h1>
                        <label for="studname">student Name</label><br>
                        <input type="text" id="studname" name="studname" placeholder="Enter stud name" required ><br>
                        <label for="studid">student id</label><br>
                        <input type="text" id="studid" name="studid" placeholder="" readonly value="%s" required><br>
                        <label for="batch">Batch</label><br>
                        <input type="text" id="batch" name="batch" placeholder="" required><br>
                        <label for="department">Department</label><br>
                        <select name="department" id="department" required>
                            <option value="">choose your department</option>
                            <option value="Electronics and Communication">Electronics and Communication</option>
                            <option value="Electrical and Electronics">Electrical and Electronics</option>
                            <option value="Mechanical">Mechanical</option>
                            <option value="civil">civil </option>
                        </select><br>
                        <label for="sem">Semester</label><br>
                        <select name="sem" id="sem" required>
                            <option value="">choose the Semester</option>
                            <option value="S1">S1</option>
                            <option value="S2">S2</option>
                            <option value="S3">S3</option>
                            <option value="S4">S4</option>
                            <option value="S5">S5</option>
                            <option value="S6">S6</option>
                            <option value="S7">S7</option>
                            <option value="S8">S8</option>                           
                            
                        </select><br>
                         <label for="dob">Date of birth</label><br>
                        <input type="date" id="dob" name="dob" placeholder="" ><br>
                        <label for="gender">Gender</label><br>
                        <input type="radio" id="male" value="male" style="width:20px;height:15px;" name="gender" required>
                        <label for="male">Male</label>
                        <input type="radio" id="female" value="female" name="gender"style="width:20px;height:15px;"required>
                        <label for="female">female</label><br>                      
                        <label for="email">Email</label><br>
                        <input type="email" id="email" name="email" placeholder="Enter email" required><br>
                        <label for="phone">Mobile Number</label><br>
                        <input type="tel" id="phone" name="phone" placeholder="Enter mobile number" ><br>
                        <label for="password">Password</label><br>
                        <input type="password" id="password" name="password" placeholder="Enter your password" required><br>
                        <input type="file" name="pic" style="border:none;"required>
                        <input type="submit" value="sign-in" name="sub">
                   </form>
                </div>
            </div>
        </div>
    </section>
    <footer class="pt-5 pt-5 mb-0">
              <div class="container-fluid container-md">
                  <div class="row ">
                      <div class="col-lg-3 col-sm-6 div-1">
                          <img src="logo-swce-white.png" class="img-fluid " width="180px">
                          <p class="mt-3">
                              Study World College of Engineering, started in 2009,
                              is one of the renowned private institutions of Coimbatore, India.
                              The college offers a range of courses approved by AICTE and affiliated to Anna University.
                              Study World College of Engineering is a part of Study World Education Holding Group.
                          </p>
                      </div>
                      <div class="col-lg-3 col-sm-6 div-2 ps-5 mt-lg-0 mt-4">
                          <h3 class="adm mb-5">Admissions</h3>
                          <a href="#">Eligibility Criteria</a>
                          <a href="#">Scholarships</a>
                          <a href="#">Admission Guidelines</a>
                          <a href="#">Accommodation & Mess</a>
                      </div>
                      <div class="col-lg-3 col-sm-6 col-12 ps-5 mt-lg-0 mt-4">
                          <h3>Gallary</h3>
                          <div class="img-grid mt-5 ">
                              <img src="1.jpg" class="img-fluid">
                              <img src="3.jpg" class="img-fluid">
                              <img src="11.jpg" class="img-fluid">
                              <img src="12.jpg" class="img-fluid">
                              <img src="14.jpg" class="img-fluid">
                              <img src="19.jpg" class="img-fluid">
                              <img src="20.jpg" class="img-fluid">
                              <img src="25.jpg" class="img-fluid">
                              <img src="26.jpg" class="img-fluid">
                          </div>
                      </div>
                      <div class="col-lg-3 col-sm-6 col-12 ps-5 mt-lg-0 mt-4">
                          <h3 class="mb-5">Contact us</h3>
                          <h5>Study World College of Engineering</h5>
                          <p>
                              1/2A-1, Alagu Nachiamman
                              Kovil Road,Palathurai,Madukkarai,
                             Coimbatore - 641105.
                          </p>
                          <p >
                              mobile:<a href="#" class="mob">+91 9944911933</a><br>
                              Email:<a href="#" class="email"> coimbatore@swehg.com</a>
                          </p>
                      </div>
                  </div>
              </div>

           </footer>

     <script>
        function logout() {
          // Perform logout logic here
        
          // Replace the current page with a new one, effectively removing it from the history
          window.location.replace("adminDashboard.py");
        }
     </script>
    <script src="https://kit.fontawesome.com/d53d2b527f.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
""" %(studid))

import cgi

f = cgi.FieldStorage()
pstudname = f.getvalue("studname")
pstudid = f.getvalue("studid")
pbatch= f.getvalue("batch")
pdep =f.getvalue("department")
psem=f.getvalue("sem")
pdob = f.getvalue("dob")
pgender = f.getvalue("gender")
pemail = f.getvalue("email")
pmob = f.getvalue("phone")
ppass = f.getvalue("password")
psub = f.getvalue("sub")

if psub != None:
   # q=""" select id,studId,email,password from stud where studId='%s' or email='%s' or password='%s'"""%(pstudid,pemail,ppass)
    #cur.execute(q)
    #result = cur.fetchall()
    #if result == None:
        ppic = f['pic']
        if ppic.filename:
            import smtplib

            fromaddr = 'akhilmkrishnan2001@gmail.com'
            toaddr = pemail
            msg = """
                Hello %s,
                you are successfully registered,
                your employee id is %s and password is %s
            """ % (pstudname, pstudid, ppass)
            password = 'snvhhehrrgihwivt'
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(fromaddr, password)
            server.sendmail(fromaddr, toaddr, msg)
            server.quit()
            import os

            fn = os.path.basename(ppic.filename)
            open("files/" + fn, "wb").write((ppic.file.read()))
            q = """ insert into stud(studName,studId,Batch,Department,Semester,dob,gender,email,mobile,password,profile)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
            pstudname, pstudid,pbatch,pdep,psem, pdob, pgender, pemail, pmob, ppass, fn)
            cur.execute(q)
            con.commit()
            print("""
                <script>
                     location.href="studExist.py"
                    alert("everything success");
                </script>
            """)
        else:
            print("""
                        <script>
                            alert("mulfunctioning...!);
                        </script>
                    """)
    #else:
       # print("""
                               ##    alert("already inserted this data...!);
                               #</script>
             #""")
con.close()



