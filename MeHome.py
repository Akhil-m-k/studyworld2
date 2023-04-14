#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

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
     <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.carousel.min.css"
      integrity="sha512-tS3S5qG0BlhnQROyJXvNjeEM4UpMXHrQfTGmbQ1gKmelCxlSEBUaxhRBj/EFTzpbP4RVSrpEikbmdJobCvhE3g=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="utility.css">
     <style>
       @media(max-width:600px){
      .navbar-brand {
          width:45%;
      }
     }

    form{
            background-color: #ffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow:0px 0px 13px rgba(0,0,0,0.5);
        }
        input{
            width: 100%;
            border-radius: 7px;
            height: 40px;
            padding-left: 15px;
            border:1px solid gray;
        }
        textarea{
            width: 100%;
            padding-left: 15px;
        }
        input:last-child{
            background-color: green;
            border: none;
            color:#ffff;
            font-weight: bold;
        }
        input:focus{
            outline: none;
        }
        iframe{
            border-radius: 10px;
            width:100%;
            min-height:440px;
            box-shadow:0px 0px 13px rgba(0,0,0,0.5);
        }
        .location{
            min-height:900px;
        }
         .location .container{
              padding-top:200px;
              padding-bottom:50px;
            }
        @media (max-width:1600px){
            .location .container{
                    padding-top:250px;
            }
        }
        @media (max-width:775px){
            .location iframe{
                margin-bottom:20px;
            }
        }
        .content h1{
            font-weight:bold;
        }
          .content p,ul li{
            font-size:15px;
            line-height:30px;
            text-align:justify;
        }
        /* know-more */


        .know-more{
            background-color:lightgray;
            padding-bottom:20px;
        }
        .know-head{
            background-color:gray;
            padding:20px 0px;
        }
        .know-more ul{
           margin:20px 30px;

        } 
         .know-more ul li{
            line-height
         }
        .know-more a{
            text-decoration:none;

        }
     </style>
</head>
<body style="height:auto;">
    <!-- head-section -->
    <div class="main-header"style="position:fixed; z-index:300; left:0px; right:0px;">
    <header >
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

    <section class="navigation" >

        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-lg container-fluid">
              <a class="navbar-brand" href="#"><img src="logo-swce (1).png " class="img-fluid" width="44%" alt=""></a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarNavDropdown">
                <ul class="navbar-nav ms-lg-auto ms-2">
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
                  <li class="nav-item ">
                   <div class="dropdown">
                      <button class="dropbtn" style="white-space: nowrap;">Login
                        <i class="fa-solid fa-caret-down icon-1"></i>
                        <i class="fa-sharp fa-solid fa-caret-up icon-2" ></i>
                      </button>
                      <div class="dropdown-content" style="z-index:200;">
                        <a href="adminLogin.py">Admin</a>
                        <a href="staffLogin.py">Staff</a>
                        <a href="studLogin.py">Student</a>
                      </div>
                    </div>
                  </li>

                      <li class="nav-item"> <a href="ContactUs.py" class="nav-link">Contact us</a></li>
                </ul>
              </div>
            </div>
          </nav>
    </section>
    </div>
    <section class="content" style="padding-top:165px; min-height:600px;">
        <div>
            <img src="images/mech.jpg" class="img-fluid w-100">
        </div>
        <div class="container pt-3">
            <div class="row">
                <div class="col-lg-8 col-12">
                    <h1>Mechanical Engineering</h1>
                    <hr>
                    <h1>Vision</h1>
                    <p>
                     To be a premier centre of technology, in the domain of Electronics and
                     Communication Engineering, at par with global standards,
                     catering to the ever changing challenges in technical education and research.
                     </p>
                     <h1>Mission</h1>
                      <p>
                            To evolve the department into global standards with top class academic
                            persons to provide state of the art knowledge to the students in various
                            mechanical engineering concepts, to adapt themselves to global needs while
                            upholding professional ethics and to contribute their might to transforming
                            India into a world leader in technology.
                       </p>
                     <h1>HOD&#39;s Message</h1>
                     <p>

                        Welcome to the Department of Mechanical Engineering at Al Ameen Engineering College.
                        We started our journey in the year of 2003. Over the last decade, we have grown our
                        expertise and competence in the core Mechanical Engineering curriculum and research.
                        We have a strong undergraduate program in mechanical engineering, including a B. Tech.
                        Our department offers science-based engineering curriculum. The primary focus of our 
                        curriculum is to impart technical knowledge, promote their problem solving skills and
                        innovation of new technologies. Department offers large number of optional courses for
                        providing wide spectrum of options to the students to pursue their interest and are 
                        encouraged to undertake novel projects as the part of their projects.Our department 
                        has a distinguished record in teaching. Faculty members have excellent academic 
                        credentials and are highly regarded. They have been conferred with many prestigious
                        awards at national and international levels. Our department has well equipped laboratories
                        which are guided by persons having years of industrial exposure.This website provides an
                        overview of the academic programs, research activities of our department, research facilities,
                        profiles of faculty members, and details of student activities. . Whether you are a prospective 
                        undergraduate or graduate student, a faculty or staff member, a former student, an industry advisor
                         or a government or industry recruiter, you&lsquo;ll find that the Department of Mechanical Engineering at AEC is a great place.
                        I am excited to see what the future holds for our department and invite you to join us on our 
                        incredible journey. The purpose of this site is to feature program information, department news 
                        and events, and items of interest. However, if you don&lsquo;t find what you are looking for, or if you
                        would like additional information, please contact me by mail, telephone, fax, or email.

                     </p>
                </div>
                <div class="col-lg-4 col-12 d-flex justify-content-center align-items-start pt-3" >
                    <div class="know-more mb-5 ms-3"style="width:100%;">
                        <h1 class="know-head text-center">Know More</h1>
                        <ul >
                            <li><a href="mechStaff.py">Staff Profile</a></li>
                            <li><a href="https://ktu.edu.in/eu/acd/viewCurriculum.htm?clusterId=JFpMR4a48zcjvofdLtNrcvn91Z2X30eT3ACu8aEDIgc%3D&programId=9fRs52bLA%2Fe53euJKX2d3kkIgGZbKN%2F4yFyzXnhTevE%3D">Syllabus</a></li>
                            <li><a href="meClsMntrs.py">Class Teachers and Mentors</a></li>
                            <li><a href="meLab.py">Lab and Facilities</a></li>
                            <li><a href="meMnrDegree.py">Minor Degree course</a></li>
                            <li><a href="eceRsrh.py">Research Publications</a></li>
                            <li><a href="meSocietyMemb.py">Society Membership</a></li>
                            <li><a href="meAddOncourse.py">Add on Courses</a></li>
                        </ul> 
                    </div>
                </div>
            </div>
        </div>
    </section>


     <!--footer-->
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