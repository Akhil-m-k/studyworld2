#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="adminDetails")
cur = con.cursor()
import cgi

f = cgi.FieldStorage()
pid = f.getvalue("id")
q = """ select staffName,staffId from staff where id='%s'"""%(pid)
cur.execute(q)
r = cur.fetchone()
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
                  <li class="nav-item dropdown">
                    <a class="nav-link" href="AboutUs.py"> About Us</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="courses.py">Courses</a>
                  </li>
                  
                  <li>
                      <div class="dropdown">
                            <button class="dropbtn" >leave
                              <i class="fa-solid fa-caret-down icon-1"></i>
                              <i class="fa-sharp fa-solid fa-caret-up icon-2" ></i>
                            </button>
                            <div class="dropdown-content">
                              <a href="staffLeave.py?id=%s">New</a>
                              <a href="staffstaffLeavefExsisting.py?id=%s">Existing</a>
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
    <section class="login">
        <div class="container pt-5 pb-5">
            <div class="row">
                <div class="col-12 d-flex justify-content-center">
                    <form action="" method="post"enctype="multipart/form-data">
                        <h1>Sign-Up</h1>
                        <label for="stfname">staff Name</label><br>
                        <input type="text" id="stfname" name="stfname" value="%s" placeholder="Enter staff name" required ><br>
                        <label for="stfid">staff id</label><br>
                        <input type="text" id="stfid" name="stfid" placeholder="" readonly value="%s"><br>
                        <label for="frdate">From Date</label> <br>
                        <input type="date" id="frdate" name="frdate" placeholder="" oninput="calculateAge() " required> <br>
                        <label for="toDate">To Date</label> <br>
                        <input type="date" id="toDate" name="toDate" placeholder="" oninput="calculateAge() " required> <br>
                        <label for="tleave">total leave</label> <br>
                        <input type="number" id="tleave" name="tleave"><br>
                        <label for="reason">Reason</label> <br>
                        <textarea col="10" row="30" class="w-100" name="reason">type something....!
                        </textarea>
                        <input type="submit" value="sign-in" name="sub">
                   </form>
                </div>
            </div>
        </div>
    </section>
    <footer class="pt-5 pt-5  mb-0">
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
    <script>
         function calculateAge() {
    const frdate = new Date(document.getElementById("frdate").value);
    const toDate= new Date(document.getElementById("toDate").value);
    const timeDiff = Math.abs(toDate.getTime() - frdate.getTime());
    const diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));
     document.getElementById("tleave").value= diffDays;
  }
    </script>
     <script>
function logout() {
  // Perform logout logic here

  // Replace the current page with a new one, effectively removing it from the history
  window.location.replace("staffDashboard.py?id=%s");
}
</script>
    </body>
    </html>
"""%(pid,pid,r[0], r[1],pid))


pstfname = f.getvalue("stfname")
pstfid = f.getvalue("stfid")
pfrdate = f.getvalue("frdate")
ptoDate= f.getvalue("toDate")
ptleave = f.getvalue("tleave")
preason = f.getvalue("reason")
psub = f.getvalue("sub")

if psub != None:

 q = """ insert into staffLeave(staffName,staffId,fromDate,toDate,totalLeave,reason,status)values('%s','%s','%s','%s','%s','%s','%s')""" % (
pstfname, pstfid, pfrdate, ptoDate, ptleave, preason,"New")
cur.execute(q)
con.commit()
print("""
            <script>
                location.href="staffstaffLeavefExsisting.py?id=%s"
                alert("everything success");
            </script>
  """%(pid))

con.close()



