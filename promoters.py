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
     .promoters{
        padding-top:175px;
     }
     .promoters .row{
       display:flex;
       justify-content:center;
     }
    .promoters .col-12{
        display:grid;
        place-items:center;
       
    }
    .promoters .col-12 div{
         border-radius:10px;
        box-shadow:0px 0px 15px rgba(0,0,0,0.5);
        padding:35px;
       
    }
    .promoters .col-12 img{
        border-radius:10px;
    }
    .promoters .col-12 h5{
        font-size:18px;
    }
     .promoters .col-12 h6{
        background-color:#333333;
    }
    @media (max-width:1220px){
        .promoters{
           padding-top:200px;
        }
    }
    @media (max-width:400px){
    .promoters{
           padding-top:240px;
        }
    .promoters .col-12 div {
        width:250px;
    }

   .promoters .col-12 div img{
        width:250px;
   }
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

<!-- promoters -->
    <section class="promoters" >
        <div class="container mt-4 mb-5">
            <div class="d-flex justify-content-center">
                <div style="display:inline-block;">
                     <h2 class="fw-bold">Promoters</h2>
                     <hr style="height:8px; border-radius:5px; background-color:blue;">
                </div>
            </div>
         <div class="row mt-5" style="row-gap:35px;" >
            
                <div class="col-12 col-lg-6 col-xxl-4">
                <div  >
                    <img src="images/Dr-Vidhya-Vinod.jpg" class="img-fluid" >
                    <h5 class="fw-bolder pt-2 text-dark text-center">DR. VIDHYA VINOD</h5>
                    <h6 class="text-white  text-center py-2">CHAIRPERSON</h6>
                </div>
                
            </div>
             <div class="col-12 col-lg-6 col-xxl-4">
                <div >
                    <img src="images/Vinod1.jpg"class="img-fluid" >
                    <h5 class="fw-bolder pt-2 text-dark text-center ">MR. VINOD NEETHAKANDAM</h5>
                    <h6 class="text-white  text-center py-2">CORRESPONDENT</h6>
                </div>
            </div>
            <div class="col-12 col-lg-6 col-xxl-4">
                <div >
                    <img src="images/Jayakrishnan.jpg" class="img-fluid">
                    <h5 class="fw-bolder pt-2 text-dark text-center">MR. S. JAYAKRISHNAN</h5>
                    <h6 class="text-white  text-center py-2">SECRETARY</h6>
                </div>
            </div>
            <div class="col-12 col-lg-6 col-xxl-4">
                <div >
                    <img src="images/karthikeyan.jpg" class="img-fluid">
                    <h5 class="fw-bolder pt-2 text-dark text-center">MR. S. KARTHIKEYAN</h5>
                    <h6 class="text-white  text-center  py-2">MANAGING TRUSTEE</h6>
                </div>
            </div>
            <div class="col-12 col-lg-6 col-xxl-4">
                <div >
                    <img src="images/Raymi-van-der-spek.jpg" class="img-fluid">
                    <h5 class="fw-bolder pt-2 text-dark text-center ">MR. RAYMI VAN DER SPEK</h5>
                    <h6 class="text-white  text-center  py-2">CHIEF OPERATING OFFICER</h6>
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