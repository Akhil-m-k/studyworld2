#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import math,random
corpus="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
generate_OTP=""
size=5
length = len(corpus)
for i in range(size):
    generate_OTP += corpus[math.floor(random.random()*length)]
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
    <style>
    .login{
       display:flex;
     justify-content:center;
     align-items:center;
     flex-direction:column;
     background-image:url('bg-2.jpeg');
     background-repeat:no-repeat;
     background-size:cover;
     height:760px;
    }
     form{
      padding:25px;
      width:500px;
      max-width:450px;
      background-color:#fff;
      border-radius:8px;
      box-shadow:0px 0px 10px black;
    }
    input{
    border:1px solid gray;
    border-radius:5px;
    margin-bottom:15px;
    height:35px;
    font-size:18px;
    padding-left:10px;
     width:100%
    }
    input:focus{
    outline:none;
    }
     .sub{
     background-color:green;
     border:none;
     border-radius:5px;
     font-weight:bold;
     color:#fff;
    }
    label{
       font-family:arial;
       font-size:18px;
       font-weight:bold;

    }
    h1{
       text-align:center;
       margin-bottom:40px;
        margin-top:15px;
    }
    form a{
        text-decoration:none;
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
              <a class="navbar-brand" href="#"><img src="logo-swce (1).png " class="img-fluid" width="44%" alt=""></a>
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
                      <li class="nav-item"> <a href="ContactUs.py" class="nav-link">Contact us</a></li>
                </ul>
              </div>
            </div>
          </nav>
    </section>
   <section class="login">
        <div class="container">
            <div class="row">
                <div class="col-md-6 col-12">
                    <h1 class="main-head " style="font-size:60px;  color:#fff; font-family:fantasy; ">STUDY WORLD <br>COLLEGE OF ENGINEERING</h1>
                </div>
                <div class="col-md-6 col-12">
                     <form method = "post" action = "">
                     <h1> Login </h1>
                     <label for ="email"> Email </label><br>
 <input type = "text"placeholder = "enter your registered email" name = "email"id = "email"> <br>
 <input type = "submit" class ="sub" value="submit" name="sub">

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


    <script src="https://kit.fontawesome.com/d53d2b527f.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
""")

import cgi

f = cgi.FieldStorage()
pemail = f.getvalue("email")
psub = f.getvalue("sub")

if psub != None:
    import mysql.connector

    conn = mysql.connector.connect(host="localhost", user="root", password="", database="adminDetails")
    cur = conn.cursor()
    q = """ select id,email from stud where email='%s'""" % (pemail)
    cur.execute(q)
    f = cur.fetchone()

    if f != None:
        import smtplib
        from email.message import EmailMessage
        msg = EmailMessage()
        msg.set_content('OTP for re-setting your password is %s '%(generate_OTP))
        msg['subject']= 'OTP Reg !!!'
        msg['from'] = "akhilmkrishnan2001@gmail.com"
        msg['to']=pemail
        password = 'snvhhehrrgihwivt'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('akhilmkrishnan2001@gmail.com', password)
        server.send_message(msg)
        server.quit()
        print("""
            <script>
            alert("otp sented successfully...!!!")
                location.href="StudOtpAccept.py?id=%s&generate_OTP=%s";
            </script>"""%(f[0],generate_OTP))
    else:
        print("""
        <script>
            alert("Please enter a registered email.....!");
        </script>
    """)
