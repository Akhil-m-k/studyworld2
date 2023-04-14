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
    <link rel="stylesheet" href="index.css">
    <link rel="stylesheet" href="width.css">
     <style>
      .navbar-nav .nav-item .nav-link:hover{
            color:orange;
      }
      .dropbtn:hover{
       color:orange;
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
              <a class="navbar-brand" href="#"><img src="logo-swce (1).png " class="img-fluid"  alt=""></a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarNavDropdown">
                <ul class="navbar-nav ms-lg-auto ms-2">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="index.html">Home</a>
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

    <section class="carousel-1">
        <!-- Modal -->
        <div id="loginModal" class="modal">
    <div class="modal-content">
      <span class="close">&times;</span>
      <h2>REGISTRATION FOR COURSE</h2>
      <form method="post" enctype="multipart/form-data">
        <label for="username">Full Name </label>
        <input type="text" id="username" name="username" placeholder="Enter your name"><br>

        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Enter your email"><br>

        <label for="mob">Mobile</label>
        <input type="tel" id="mob" name="mob" placeholder="Enter your phone number"><br>

        <label for="course">Select Course</label>
        <select name="course" id="course">
          <option value="">select course</option>
          <option value="B.E Mechanical Engineering">B.E Mechanical Engineering</option>
          <option value="B.E Electronics and Communication Engineering">B.E Electronics and Communication Engineering</option>
          <option value="B.E Electrical and Electronics Engineering">B.E Electrical and Electronics Engineering</option>
          <option value="B.E Computerscience and Engineering">B.E Computerscience and Engineering</option>
        </select>

        <input type="submit" name="sub" value="Register">
      </form>
    </div>
  </div>
        <section class="marque">
            <marquee direction="left" style="font-size:25px; color: orangered; font-weight:bold;">
                Study world Engineering College 2023 Admission Started for b.tech students
            </marquee>
        </section>
            <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">

                <div class="carousel-inner">
                  <div class="carousel-item active"  >
                    <img src="img-1.jpg" class="d-block w-100 img-fluid img-1"  alt="..." style="max-height: 800px;">
                    <div class="carousel-caption mt-5" >
                        <h6>STUDY WORLD GROUP</h6>
                      <h1>Study World College Of Engineering,</h1>
                      <h2 class="mt-3">Your Future Begins Here</h2>
                      <button class="btn btn-primary mt-4"  id="loginBtn">Enqire Now</button>

                    </div>
                    <img src="slider-university-layer.png " class="img-fluid img-2"  alt="">
                  </div>
                  <div class="carousel-item">
                    <img src="img-2.jpg" class="d-block w-100 img-fluid" alt="..."style="max-height: 800px;">
                    <div class="carousel-caption  d-md-block">
                        <h6>STUDY WORLD GROUP OF COLLEGES</h6>
                        <h1>Admission Started</h1>
                        <h2 class="mt-3" style="font-weight: bold; ">For 2023-24 Batch</h2>
                        <h3 class="mb-5  mt-4 ">Admission open for 2023-24 batches</h3>
                        <button class="btn btn-primary mt-1 mt-md-4 me-md-5 me-1" id="loginBtn2" >Apply Now</button>
                        <a href="courses.py"><button class="btn btn-2 btn-primary  mt-1 mt-md-4">Learn More</button></a>
                    </div>
                    <img src="slider-university-layer.png " class="img-fluid img-2"  alt="">
                  </div>
                  <div class="carousel-item" >
                    <img src="img-3.jpg" class="d-block w-100 img-fluid" alt="..."style="max-height: 800px;">
                    <div class="carousel-caption d-md-block ">
                        <h6>STUDY WORLD GROUP OF EDUCATIONAL INSTITUTIONS</h6>
                        <h1 class="mt-3 mb-2 mb-md-3">Our Educational <br> Programs</h1>
                        <h2 class="mt-3 mb-3 mb-md-5">Our Engineering Undergraduate Programs</h2>
                        <button class="btn btn-primary mt-1 mt-md-4 me-md-5 me-1" id="loginBtn3" >Apply Now</button>
                        <a href="courses.py"><button class="btn btn-2 mt-1 mt-md-4" >Learn More</button></a>
                    </div>
                    <img src="slider-university-layer.png " class="img-fluid img-2"  alt="">
                  </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                  <span class="visually-hidden">Next</span>
                </button>
              </div>
        </section>

       <!-- College explore-->

         <section class="pt-4 ps-3 pe-3 text-center experience " >
      <div class="container-fluid container-xl">
         <div class="d-flex justify-content-center mb-4">
             <div style="display:inline-block">
                 <h2 >Explore College</h2>
                 <hr style="height:8px;text-align:center; border-radius:5px; background-color:blue;">
             </div>
        </div>
           <div class="owl-carousel owl-1 owl-theme pt-3">
              <div class="item position-relative">
                 <img src="owl-1.jpeg" class="img-fluid" alt="" />
                    <h2 class="position-absolute inner-head fw-bold">TEACHERS</h2>
                      <div class="inner position-absolute top-0 w-100 h-100">
                        <p class="text-center">
                          "Teaching is a profession that teaches all other professions",
                            We provide highly qualified , effective and student friendly teachers.
                        </p>
                      </div>
                        <div class="border-btm border-1 position-absolute bottom-0"></div>
                          <div class="position-absolute null-div null-div-1"></div>
              </div>
              <div class="item position-relative">
                <img src="owl-2.jpeg" class="img-fluid" alt="" />
                  <h2 class="position-absolute inner-head fw-bold">GAMES</h2>
                    <div class="inner position-absolute top-0 w-100 h-100">
                      <p class="text-center">
                        "Games improve the talent of students "
                          we are providing all types of game facilities here.
                      </p>
                    </div>
                      <div class="border-btm border-2 position-absolute bottom-0"></div>
                      <div class="position-absolute null-div null-div-2"></div>
              </div>
              <div class="item position-relative">
                <img src="owl-3.jpeg" class="img-fluid" alt="" />
                  <h2 class="position-absolute inner-head fw-bold">LIBRARY</h2>
                    <div class="inner position-absolute top-0 w-100 h-100">
                      <p class="text-center">
                        We provide a open library to students with more space and all other
                          facilities.
                      </p>
                    </div>
                      <div class="border-btm border-3 position-absolute bottom-0"></div>
                      <div class="position-absolute null-div null-div-3"></div>
              </div>
              <div class="item position-relative">
                <img src="owl-4.jpeg" class="img-fluid" alt="" />
                  <h2 class="position-absolute inner-head fw-bold">LAB</h2>
                    <div class="inner position-absolute top-0 w-100 h-100">
                      <p class="text-center">
                        Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                          Dolores ipsa aspernatur nobis? Eum,
                          ducimus  ex id unde at officia a possimus laborum placeat.
                      </p>
                    </div>
                      <div class="border-btm border-4 position-absolute bottom-0"></div>
                      <div class="position-absolute null-div null-div-4"></div>
              </div>
              <div class="item position-relative">
                <img src="owl-5.jpeg" class="img-fluid" alt="" />
                  <h2 class="position-absolute inner-head fw-bold">CLASS ROOM</h2>
                    <div class="inner position-absolute top-0 w-100 h-100">
                      <p class="text-center">
                        Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                          Dolores ipsa aspernatur nobis? Eum,
                          ducimus  ex id unde at officia a possimus laborum placeat.
                      </p>
                    </div>
                      <div class="border-btm border-5 position-absolute bottom-0"></div>
                      <div class="position-absolute null-div null-div-5"></div>
              </div>
              <div class="item position-relative">
                <img src="owl-6.jpeg" class="img-fluid" alt="" />
                  <h2 class="position-absolute inner-head fw-bold">HOSTEL</h2>
                    <div class="inner position-absolute top-0 w-100 h-100">
                      <p class="text-center">
                        Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                          Dolores ipsa aspernatur nobis? Eum,
                          ducimus  ex id unde at officia a possimus laborum placeat.
                      </p>
                    </div>
                      <div class="border-btm border-6 position-absolute bottom-0"></div>
                      <div class="position-absolute null-div null-div-6"></div>
              </div>
        </div>
      </div>
      <button type="button" class="text-white explore-btn mt-4">
        FIND MORE EXPERIENCES <strong> &#62;</strong>
      </button>

     <section class="container mt-5">
         <div style="display:inline-block;">
             <h2>Welcome to study world</h2>
             <hr style="height:8px; border-radius:5px; background-color:blue;">
         </div>
         <p style="text-align:justify; font-size:18px; color:#09347a;">
             Study World is one of the leading educational advisory centres in SouthIndia, offering services all ovr India & Abroad for career
             counselling and Admission guidance through comprehensive expertise and excellence in the field Education
             Study world takes peasure in providin admission guidance in most of the reputed institutions
             offering education in every sphere and many more. We provide all – around assitance for studens to get
             admission in various Professional course under Management / NRI Quota.
             Study world offers a unique of serice dedicated to advising, councelling and guiding candidates.</p>
     </section>

             <!-- card section-->

     <section class="container mt-5">

         <div class="row" style=" row-gap:15px;">
             <div class="col-lg-4 col-sm-6 col-12" style=" display:flex; justify-content:center;">
                 <div class="card" style="width: 18rem;">
                      <div>
                            <img class="card-img-top" src="counselling.jpg">
                      </div>
                      <div class="card-body">
                        <h5 class="card-title text-dark"> COUNSELLING</h5>
                        <p class="card-text">Free educational counselling to students and parents regarding all courses.</p>

                      </div>
                 </div>
             </div>
             <div class="col-lg-4 col-sm-6 col-12"style=" display:flex; justify-content:center;">
                  <div class="card" style="width: 18rem;">
                      <img class="card-img-top" src="19.jpg">
                      <div class="card-body">
                        <h5 class="card-title text-dark">INSTITUTES</h5>
                        <p class="card-text">We guide and prefer recognized and well-known institutions only.</p>

                      </div>
                 </div>
             </div>
             <div class="col-lg-4 col-sm-6 col-12"style=" display:flex; justify-content:center;">
                  <div class="card" style="width: 18rem;">
                      <img class="card-img-top" src="admission.jpg">
                      <div class="card-body">
                        <h5 class="card-title text-dark">ADMISSION PROCESS</h5>
                        <p class="card-text">Analyzing and sorting out application requirements for admission process.</p>

                      </div>
                 </div>
             </div>
             <div class="col-lg-4 col-sm-6 col-12"style=" display:flex; justify-content:center;">
                  <div class="card" style="width: 18rem;">
                      <img class="card-img-top" height="180px" src="careeer.png">
                      <div class="card-body">
                        <h5 class="card-title text-dark">CAREER COUNSELLING</h5>
                        <p class="card-text">One to one career counselling, choosing & selecting courses, colleges & universities.</p>

                      </div>
                 </div>
             </div>
             <div class="col-lg-4 col-sm-6 col-12"style=" display:flex; justify-content:center;">
                  <div class="card" style="width: 18rem;">
                      <img class="card-img-top" src="guidence.jpg">
                      <div class="card-body">
                        <h5 class="card-title text-dark">SPECIAL GUIDANCE</h5>
                        <p class="card-text">Special guidance is given to overseas students joining colleges and universities in India and other countries.</p>

                      </div>
                 </div>
             </div>
             <div class="col-lg-4 col-sm-6 col-12"style=" display:flex; justify-content:center;">
                  <div class="card" style="width: 18rem; ">
                      <img class="card-img-top" src="scholarship.jpg">
                      <div class="card-body">
                        <h5 class="card-title text-dark">SCHOLARSHIP</h5>
                        <p class="card-text">We offer Scholarship those who are taking admission through Study World</p>

                      </div>
                 </div>
             </div>
         </div>
     </section>

             <!--Photo Gallery-->

    </section>
    <section class="photo-galary mb-5 mt-5">
        <div class="d-flex justify-content-center ">

             <div style="display:inline-block">
                 <h2 >Explore Photo Galary</h2>
                 <hr style="height:8px;text-align:center; border-radius:5px; background-color:blue;">
             </div>

        </div>
      <div class="container-fluid">

        <div class="row gx-0">
          <div class="col-xl-2 col-md-3 col-6" >
            <div class="position-relative">
              <a href=""><img src="ph-1.jpg" class="img-fluid w-100" alt=""></a>
            <div class="position-absolute  w-100 photo">
              <h5 class="text-center ">Inner college</h5>
            </div>
            </div>
          </div>
          <div class="col-xl-2 col-md-3 col-6">
            <div class="position-relative">
              <a href=""><img src="ph-2.jpg" class="img-fluid w-100" alt=""></a>
            <div class="position-absolute  w-100 photo">
              <h5 class="text-center">open way</h5>
            </div>
            </div>
          </div>
          <div class="col-xl-2 col-md-3 col-6">
            <div class="position-relative">
              <a href=""><img src="ph-3.jpg" class="img-fluid w-100" alt=""></a>
            <div class="position-absolute  w-100 photo">
              <h5 class="text-center ">Office building</h5>
            </div>
            </div>
          </div>
          <div class="col-xl-2 col-md-3 col-6">
            <div class="position-relative">
              <a href=""><img src="ph-4.jpg" class="img-fluid w-100" alt=""></a>
            <div class="position-absolute  w-100 photo">
              <h5 class="text-center ">
                principal cabin
              </h5>
            </div>
            </div>
          </div>
          <div class="col-xl-2 col-md-3 col-6">
            <div class="position-relative">
              <a href=""><img src="ph-5.jpg" class="img-fluid w-100" alt=""></a>
            <div class="position-absolute  w-100 photo">
              <h5 class="text-center ">medicine department</h5>
            </div>
            </div>
          </div>
          <div class="col-xl-2 col-md-3 col-6">
            <div class="position-relative">
              <a href=""><img src="ph-6.jpg" class="img-fluid w-100" alt=""></a>
            <div class="position-absolute  w-100 photo">
              <h5 class="text-center ">Guest room</h5>
            </div>
            </div>
          </div>
          <div class="col-xl-2 col-md-3 col-6 " >
            <div class="position-relative">
              <a href=""><img src="ph-7.jpg" class="img-fluid w-100" alt=""></a>
            <div class="position-absolute  w-100 photo">
              <h5 class="text-center ">Hostel</h5>
            </div>
            </div>
          </div>
          <div class="col-xl-2 col-md-3 col-6 ">
            <div class="position-relative">
              <a href=""><img src="ph-8.jpg" class="img-fluid w-100" alt=""></a>
            <div class="position-absolute  w-100 photo">
              <h5 class="text-center">Eng building</h5>
            </div>
            </div>
          </div>
          <div class="col-xl-2 col-md-3 col-6">
            <div class="position-relative">
              <a href=""><img src="ph-9.jpg" class="img-fluid w-100" alt=""></a>
            <div class="position-absolute  w-100 photo">
              <h5 class="text-center ">coridoor</h5>
            </div>
            </div>
          </div>
          <div class="col-xl-2 col-md-3 col-6 ">
            <div class="position-relative">
              <a href=""><img src="ph-10.jpg" class="img-fluid w-100 " alt=""></a>
            <div class="position-absolute  w-100 photo">
              <h5 class="text-center ">
                visitors section
              </h5>
            </div>
            </div>
          </div>
          <div class="col-xl-2 col-md-3 col-6">
            <div class="position-relative">
              <a href=""><img src="ph-11.jpg" class="img-fluid w-100" alt=""></a>
            <div class="position-absolute  w-100 photo">
              <h5 class="text-center ">Attender section</h5>
            </div>
            </div>
          </div>
          <div class="col-xl-2 col-md-3 col-6">
            <div class="position-relative">
              <a href=""><img src="ph-12.jpg" class="img-fluid w-100" alt=""></a>
            <div class="position-absolute  w-100 photo">
              <h5 class="text-center ">Meeting Room</h5>
            </div>
            </div>
          </div>
        </div>
      </div>
      <div class="text-center py-1">
        <button type="button" class="text-white explore-btn mt-5 mb-5">
          BROWSER OUR GALARY &nbsp;<i class="fa-solid fa-image"></i>
       </button>
     </section>
    <!-- connect with us-->
     <section class="connect-us mb-5 mt-4">
      <div class="container">
         <div class="d-flex justify-content-center mb-4">
             <div style="display:inline-block">
                 <h2 >connect with us</h2>
                 <hr style="height:8px;text-align:center; border-radius:5px; background-color:blue;">
             </div>
        </div>
        <ul class="list social-media-icons d-flex ps-0">
          <li class="rounded-circle list-item item-1">
            <a href="https://www.youtube.com/channel/UCbMkk05LuXRiq8AihxMTICQ"><i class="fa-brands fa-youtube fa-2x text-white"></i></a>
          </li>
          <li class="rounded-circle list-item item-2">
            <a href="https://www.facebook.com/studyworldeng/"><i class="fa-brands fa-facebook-f fa-2x text-white"></i></a>
          </li>
          <li class="rounded-circle list-item item-3">
            <a href="https://twitter.com/StudyWorldcbe"><i class="fa-brands fa-twitter text-white fa-2x "></i></a>
          </li>
          <li class="rounded-circle list-item item-4">
            <a href="https://www.instagram.com/studyworldeng/?hl=en"><i class="fa-brands fa-instagram fa-2x text-white"></i></a>
          </li>
          <li class="rounded-circle list-item item-5">
            <a href=""><i class="fa-brands fa-whatsapp fa-2x text-white"></i></a>
          </li>
          <li class="rounded-circle list-item item-6">
            <a href="https://www.pinterest.com/studyworldcolle/"><i class="fa-brands fa-pinterest-p fa-2x text-white"></i></a>
          </li>
          <li class="rounded-circle list-item item-7">
            <a href="https://www.linkedin.com/in/swce/?originalSubdomain=in"><i class="fa-brands fa-linkedin-in fa-2x text-white"></i></a>
          </li>
        </ul>


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



    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"
      integrity="sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/owl.carousel.min.js"
      integrity="sha512-bPs7Ae6pVvhOSiIcyUClR7/q2OAsRiovw4vAkX+zJbw3ShAeeqezq50RIIcIURq7Oa20rW2n2q+fyXBNcU9lrw=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    ></script>
    <script src="https://kit.fontawesome.com/d53d2b527f.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>

   <!-- initialisation of owl carousel-->
    <script type="text/javascript">
      $(".owl-1").owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        autoplay: true,
        responsive: {
          0: {
            items: 1,
          },
          480: {
            items: 2,
          },
          700:{
            items: 3,
          },
          1100: {
            items: 4,
          },
        },
      });
      </script>
     <script>
         // Get the modal element
var modal = document.getElementById("loginModal");

// Get the button that opens the modal
var btn = document.getElementById("loginBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
  document.body.classList.add("modal-open");
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
  document.body.classList.remove("modal-open");
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
    document.body.classList.remove("modal-open");
  }
}
     </script>
 <script>
         // Get the modal element
var modal = document.getElementById("loginModal");

// Get the button that opens the modal
var btn = document.getElementById("loginBtn2");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
  document.body.classList.add("modal-open");
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
  document.body.classList.remove("modal-open");
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
    document.body.classList.remove("modal-open");
  }
}
     </script>
 <script>
         // Get the modal element
var modal = document.getElementById("loginModal");

// Get the button that opens the modal
var btn = document.getElementById("loginBtn3");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
  document.body.classList.add("modal-open");
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
  document.body.classList.remove("modal-open");
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
    document.body.classList.remove("modal-open");
  }
}
     </script>


</body>
</html>
""")

import cgi
f =cgi.FieldStorage()
uname = f.getvalue("username")
pemail = f.getvalue("email")
pmob = f.getvalue("mob")
pcourse = f.getvalue("course")
psub = f.getvalue("sub")

if psub != None:
    import mysql.connector

    con = mysql.connector.connect(host="localhost", user="root", password="", database="adminDetails")
    cur = con.cursor()

    q=""" insert into register(fullName,Email,Mobile,Course)values('%s','%s','%s','%s')"""%(uname,pemail,pmob,pcourse)
    cur.execute(q)
    con.commit()
    if pcourse ==  "B.E Electronics and Communication Engineering":
        print("""
            <script>
                location.href="eceHome.py"
                alert("successfully registered....!");
            </script>
        """)
    elif pcourse == "B.E Mechanical Engineering":
        print("""
                   <script>
                       location.href="MeHome.py"
                       alert("successfully registered....!");
                   </script>
               """)
    elif pcourse == "B.E Electrical and Electronics Engineering":
        print("""
                   <script>
                       location.href="MeHome.py"
                       alert("successfully registered....!");
                   </script>
               """)
    elif pcourse == "B.E Computerscience and Engineering":
        print("""
                   <script>
                       location.href="MeHome.py"
                       alert("successfully registered....!");
                   </script>
               """)
