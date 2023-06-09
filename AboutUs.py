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
         .inner{
    color: #fff;
    opacity: 0;
    z-index: 100;
}
 .item:hover .inner{
    opacity: 1;
}

.inner-head{
    width: 100%;
    color: #fff;
    top: 80%;
    text-align: center;
    z-index: 100;
}

.inner p{
    padding-top: 35%;
     padding-left: 15px;
     padding-right: 18px;
}

.item:hover p{
    padding-top: 50%;
    transition: all .4s ease-in;
}

.border-btm{
    width: 100%;
    content: '';
}

.null-div{
    content: '';
    width: 100%;
    height: 350px;
    bottom: 0;
    opacity: 0;
}

.item:hover .null-div{
    height:100%;
    opacity: 1;
    transition: all .4s ease-in;
}

/* responsive carousel */
@media (max-width:1220px){
    .carousel-caption{
        position: absolute;
        top: 190px;
    }

    .carousel-item h6{
        background-color: orange;
        display: inline-block;
        color: #fff;
        font-weight: bold;
        padding: 8px 30px;
        border-radius: 8px;
        animation: btm-to-tp 1s ease-in  forwards;
        opacity: 0;
    }

    .carousel-item h1{
        font-size: 50px;
        font-weight: bold;
        font-family: Arial, Helvetica, sans-serif;
        animation: btm-to-tp-2 1s ease-in .3s forwards;
        opacity: 0;

    }

    .carousel-item h2{
        animation: btm-to-tp-3 1s ease-in .7s forwards;
        opacity: 0;
        font-size: 40px;
    }

    .carousel-item h3{
        animation: btm-to-tp-5 1s ease-in 1s forwards;
        opacity: 0;
    }

    .carousel-item button{
        padding: 18px 30px;
        outline: none;
        border: none;
        font-weight: bold;
        animation: btm-to-tp-4 1s ease-in 1.3s forwards;
        opacity: 0;

    }

    .carousel-item .btn-2{
        background-color: #fff;
        color: black;
    }
    .carousel-item .img-2{
        position: absolute;
        bottom: 0;
        right: 0;
        animation: btm-to-tp-6 1s ease-in 2s forwards;
        opacity: 0;
        width: 360px;
    }

}
@media (max-width:800px){
    .carousel-caption{
        position: absolute;
        top: 100px;
    }

    .carousel-item h6{
        background-color: orange;
        display: inline-block;
        color: #fff;
        font-weight: bold;
        padding: 8px 25px;
        border-radius: 8px;
        animation: btm-to-tp 1s ease-in  forwards;
        opacity: 0;
    }

    .carousel-item h1{
        font-size: 30px;
        font-weight: bold;
        font-family: Arial, Helvetica, sans-serif;
        animation: btm-to-tp-2 1s ease-in .3s forwards;
        opacity: 0;

    }

    .carousel-item h2{
        animation: btm-to-tp-3 1s ease-in .7s forwards;
        opacity: 0;
        font-size: 30px;
    }

    .carousel-item h3{
        animation: btm-to-tp-5 1s ease-in 1s forwards;
        opacity: 0;
    }

    .carousel-item button{
        padding: 18px 24px;
        outline: none;
        border: none;
        font-weight: bold;
        animation: btm-to-tp-4 1s ease-in 1.3s forwards;
        opacity: 0;

    }

    .carousel-item .btn-2{
        background-color: #fff;
        color: black;
    }
    .carousel-item .img-2{
        position: absolute;
        bottom: 0;
        right: 0;
        animation: btm-to-tp-6 1s ease-in 2s forwards;
        opacity: 0;
        width: 300px;
    }

}
@media (max-width:550px){
    .carousel-caption{
        position: absolute;
        top: 50px;
    }
    }
    /* about Us */
    .aboutUs img{
        margin-top:40px;
        padding-left:40px;
    }
    @media (max-width:600px){
        .aboutUs img{
          margin-top:0px;
        padding-left:0px;
    }
    }
    /* management */
    .management {
        background: url('sky-1.jpg') no-repeat center  fixed;
        height:auto;
    }
    .management img{
        border:5px solid #fff;
        border-radius:20px;
    }
    .management .col-12{
        display:flex;
        flex-direction:column;
        justify-content-center;
        align-items:center;
    }
    /* our courses */
      .courses button{
        background-color:lightgray;
        color:#fff;
        padding:11px 28px;
        border:none;
     }
     .courses button:focus{
        background-color:orange;
     }
     #div-1,#div-2,#div-3{
        padding:20px;
     }
     #div-2,#div-3{
      display:none;
     }
     .courses span,h6{
        font-weight:bold;
    }
    
    /* our toutors */
    .staffs{
      background: url('staffs.jpg') no-repeat center  fixed;
      height:auto;
    }
    .staffs img{
        border:5px solid #fff;
        border-radius:20px;
    }
     .staffs .col-12{
        display:flex;
        flex-direction:column;
        justify-content-center;
        align-items:center;
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

    <section style="position:relative; top:165px;">
            <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">

                <div class="carousel-inner">
                  <div class="carousel-item active"  >
                    <img src="img-1.jpg" class="d-block w-100 img-fluid img-1"  alt="..." style="max-height: 800px;">
                    <div class="carousel-caption " >
                        <h6>STUDY WORLD GROUP</h6>
                      <h1>SWET</h1>
                      <h1 class="mt-3">Study World Educational Trust</h1>
                     
                    </div>
                    <img src="slider-university-layer.png " class="img-fluid img-2"  alt="">
                  </div>
                  
              </div>
        </section>
        
        <!-- about us -->
        
        <section class="mt-5 pt-5 container aboutUs">
            <div class="row">
                <div class="col-lg-6 col-12 pt-5">
                     <div class="d-flex justify-content-start  pt-4 pb-4">
                         <div style="display:inline-block" class="pt-4">
                             <h2 class="text-dark fw-bold">ABOUT US</h2>
                             <hr style="height:6px;text-align:center; border-radius:5px; margin-top:-4px; background-color:orange;">
                         </div>
                     </div>
                     <h2>Study World Educational Trust</h2>
                     <p class="" style="text-align:justify;">
                        The trust was started in the year 2008 to promote education through Engineering Colleges,
                         Polytechnics, ITIS, Industrial Schools, Industrial Training Centres, Agricultural Colleges,
                        Agricultural Training Centres, Skill Training Centres, Business School,
                        Computer Training Centres etc., to provide education and training to general public. 
                        The trust is running an engineering college under the name of Study World College of Engineering
                        since 2009 and it has started SWET Project under Indian Government to conduct skill development
                        programmes/courses in Study World College Campus.We are offering free training with free accommodation
                        and food to eligible candidates along with placement opportunities upon successful completion of the 
                        courses as per the Government of India SWET project.The same leadership also manages several other institutions
                        present globally under the Study World Education Holding Group in addition to Flowers TV and Twenty Four News TV channels.
                     </p>
                </div>
                <div class="col-lg-6 col-12 " >
                    <img src="aboutus.jpg" width="100%"  class="pt-5 " height="100%">
                </div>               
            </div>
        </section>
        
        <!-- Management-->
        
        <section class="management mt-5 ">
            <div class="container pb-5">
                <div class="d-flex justify-content-center  pt-4 pb-4">
             <div style="display:inline-block">
                 <h2 class="text-white fw-bold">MANAGEMENT</h2>
                 <hr style="height:8px;text-align:center; border-radius:5px; background-color:#fff;">
             </div>
        </div>
                <div class="row">
                    <div class="col-12  " >
                        <div>
                            <img src="vidhya-vinod.jpg" width="250px" height="250px">
                        </div>
                        <div style="display:inline-block;">
                            <h3 class="text-center fw-bold pt-2 text-white">Vidhya Vinod</h3>
                            <hr class=" " style="height:5px; background-color:#fff; margin-top:-5px;">
                            <h5 class="text-center text-white" style="margin-top:-9px;">Chairperson</h5>
                        </div>
                    </div>
                </div>
                <div class="row mt-5">
                    <div class="col-lg-4 col-12 col-sm-6 mb-lg-0 mb-5 ">
                        <div>
                            <img src="Gomathy.jpeg" width="250px" height="250px">
                        </div>
                        <div style="display:inline-block;">
                            <h3 class="text-center fw-bold pt-2 text-white">Dr. P Gomathy</h3>
                            <hr class=" " style="height:5px; background-color:#fff; margin-top:-5px;">
                            <h5 class="text-center text-white" style="margin-top:-9px;">State Head</h5>
                        </div>
                    </div>
                    <div class="col-lg-4 col-12 col-sm-6 mb-lg-0 mb-5">
                        <div>
                            <img src="Manoharan.jpg" width="250px" height="250px">
                        </div>
                        <div style="display:inline-block;">
                            <h3 class="text-center fw-bold pt-2 text-white">Manoharan</h3>
                            <hr class=" " style="height:5px; background-color:#fff; margin-top:-5px;">
                            <h5 class="text-center text-white" style="margin-top:-9px;">Center Head</h5>
                        </div>
                    </div>
                    <div class="col-lg-4 col-12 col-sm-6mb-lg-0 mb-5">
                        <div>
                            <img src="Sandhya.jpg" width="250px" height="250px">
                        </div>
                        <div style="display:inline-block;">
                            <h3 class="text-center fw-bold pt-2 text-white">Sandhya</h3>
                            <hr class=" " style="height:5px; background-color:#fff; margin-top:-5px;">
                            <h5 class="text-center text-white" style="margin-top:-9px;">MIS</h5>
                        </div>
                    </div>
                </div>
            </div>
     </section>
     <!-- our Courses-->
     <section class="courses container">
        <div class="d-flex justify-content-center  pt-4 pb-4">
             <div style="display:inline-block">
                 <h2 class="text-dark fw-bold">OUR COURSES</h2>
                 <hr style="height:8px;text-align:center; border-radius:5px; background-color:orange;">
             </div>
        </div>
        <div>
            <button id="btn-1" onclick="btn1()">Aerospace CNC Machinist</button>
            <button id="btn-2"onclick="btn2()">Junior Software Devoloper</button>
            <button id="btn-3"onclick="btn3()">Sociel Media Manager</button>
            <div style="border:1px solid gray;" id="div-1">
                <p> Certification &#8211;<span>Aerospace CNC Machinist</span></p>
                <p>Additional Trade &#8211; &#8211;<span>Not Applicable</span></p>
                <p>Educational Qualifications &#8211;<span>ITI in Machanical</span></p>
                <p>Course Duration  &#8211;<span>820 Hours</span></p>
                <p>Minimum Age &#8211;<span> 21 Years</span></p>
                <p>Experience &#8211;<span>Not Applicable</span></p>
                <br>
                <h6>Basic Job Description:</h6>
                <p>
                    This role primarily involves CNC machining of aerospace
                    components/ structures in all pre-machining & post machining
                    stages along with self inspection & gauging.
                  </p>
                <h6>Eligibility Criteria</h6>
                 <ul>
                    <li>
                        These courses are exclusively for Rural profile candidates belonging to Grama 
                        Panchayat.
                    </li>
                    <li>
                        Candidates between the age 18 to 35 in the BPL category are eligible to join.
                    </li>
                    <li>
                            If the candidate belongs to APL category, there should be a Kudumbasree
                             Membership holder within immediate family members.
                    </li>
                 </ul>
                <h6>Selection Process</h6>
                 <ul>
                    <li>
                       Selection will happen at respective Panchayats.
                    </li>
                    <li>
                        Mobilization Officer visits Panchayats and reaches out to candidates 
                        via Kudumbasree Officials and Block Coordinators.
                    </li>
                    <li>
                            Eligible candidates that qualify in the initial assessment and 
                            interview will be assigned course according to their interest depending
                             on available seats in batch.
                    </li>
                 </ul>
            </div>
            <div style="border:1px solid gray;" id="div-2">
                <p> Trade of  &#8211;<span> Junior Software Devoloper</span></p>
                <p>Additional Trade &#8211; &#8211;<span>Technical Support Engineer</span></p>
                <p>Educational Qualifications &#8211;<span>B.TECH/BE/BCA</span></p>
                <p>Course Duration  &#8211;<span>960 Hours</span></p>
                <p>Minimum Age &#8211;<span> 21 Years</span></p>
                <p>Experience &#8211;<span>Not Applicable</span></p>
                <br>
                <h6>Basic Job Description:</h6>
                <p>
                    Junior Software Developers are entry-level software developers that
                    assist the development team with all  aspects of software design and coding.
                    Their primary role is to learn the codebase, attend design meetings, write 
                    basic code, fix bugs, and assist the Development Manager in all design-related tasks.
                  </p>
                <h6>Eligibility Criteria</h6>
                 <ul>
                    <li>
                        These courses are exclusively for Rural profile candidates belonging to Grama 
                        Panchayat.
                    </li>
                    <li>
                        Candidates between the age 18 to 35 in the BPL category are eligible to join.
                    </li>
                    <li>
                            If the candidate belongs to APL category, there should be a Kudumbasree
                             Membership holder within immediate family members.
                    </li>
                 </ul>
                <h6>Selection Process</h6>
                 <ul>
                    <li>
                       Selection will happen at respective Panchayats.
                    </li>
                    <li>
                        Mobilization Officer visits Panchayats and reaches out to candidates 
                        via Kudumbasree Officials and Block Coordinators.
                    </li>
                    <li>
                            Eligible candidates that qualify in the initial assessment and 
                            interview will be assigned course according to their interest depending
                             on available seats in batch.
                    </li>
                 </ul>
            </div>
            <div style="border:1px solid gray;" id="div-3">
                <p> Trade of Certification &#8211;<span> Sociel Media Manager</span></p>
                <p>Additional Trade &#8211; &#8211;<span>Not Applicable</span></p>
                <p>Educational Qualifications &#8211;<span>Any Degree</span></p>
                <p>Course Duration  &#8211;<span>700 Hours</span></p>
                <p>Minimum Age &#8211;<span> 21 Years</span></p>
                <p>Experience &#8211;<span>Not Applicable</span></p>
                <br>
                <h6>Basic Job Description:</h6>
                <p>
                    A Digital Marketing Manger is a professional who is responsible
                    for maintaining a brand’s online presence and sales by working on 
                    various marketing campaigns. Their duties include researching, strategizing
                    with other professionals and creating content for successful campaigns.
                  </p>
                <h6>Eligibility Criteria</h6>
                 <ul>
                    <li>
                        These courses are exclusively for Rural profile candidates belonging to Grama 
                        Panchayat.
                    </li>
                    <li>
                        Candidates between the age 18 to 35 in the BPL category are eligible to join.
                    </li>
                    <li>
                            If the candidate belongs to APL category, there should be a Kudumbasree
                             Membership holder within immediate family members.
                    </li>
                 </ul>
                <h6>Selection Process</h6>
                 <ul>
                    <li>
                       Selection will happen at respective Panchayats.
                    </li>
                    <li>
                        Mobilization Officer visits Panchayats and reaches out to candidates 
                        via Kudumbasree Officials and Block Coordinators.
                    </li>
                    <li>
                            Eligible candidates that qualify in the initial assessment and 
                            interview will be assigned course according to their interest depending
                             on available seats in batch.
                    </li>
                 </ul>
            </div>
        </div>
     </section>
     
     <!--our staffs-->
     
     <section class="staffs mt-5">
            <div class="container pb-5">
                <div class="d-flex justify-content-center  pt-4 pb-4">
             <div style="display:inline-block">
                 <h2 class="text-white fw-bold">OUR TRAINERS</h2>
                 <hr style="height:8px;text-align:center; border-radius:5px; background-color:#fff;">
             </div>
        </div>
                <div class="row mt-5" style="display:flex; justify-content:center; align-items-center; ">
                    <div class="col-lg-4 col-12 col-sm-6 mb-lg-0 mb-5 ">
                        <div>
                            <img src="siva.png" width="250px" height="250px">
                        </div>
                        <div style="display:inline-block;">
                            <h3 class="text-center fw-bold pt-2 text-white">Siva</h3>
                            <hr class=" " style="height:5px; background-color:#fff; margin-top:-5px;">
                            <h5 class="text-center text-white" style="margin-top:-9px;">JSD Trainer</h5>
                        </div>
                    </div>
                    <div class="col-lg-4 col-12 col-sm-6mb-lg-0 mb-5">
                        <div>
                            <img src="images/deepika.jpg" width="250px" height="250px">
                        </div>
                        <div style="display:inline-block;">
                            <h3 class="text-center fw-bold pt-2 text-white">Deepika</h3>
                            <hr class=" " style="height:5px; background-color:#fff; margin-top:-5px;">
                            <h5 class="text-center text-white" style="margin-top:-9px;">SM Trainer</h5>
                        </div>
                    </div>
                    <div class="col-lg-4 col-12 col-sm-6 mb-lg-0 mb-5">
                        <div>
                            <img src="Anjali.jpg" width="250px" height="250px">
                        </div>
                        <div style="display:inline-block;">
                            <h3 class="text-center fw-bold pt-2 text-white">Anjali</h3>
                            <hr class=" " style="height:5px; background-color:#fff; margin-top:-5px;">
                            <h5 class="text-center text-white" style="margin-top:-9px;">IT Trainer</h5>
                        </div>
                    </div>
                    <div class="col-lg-4 col-12 col-sm-6mb-lg-0 mb-5">
                        <div>
                            <img src="Anjana.jpeg" width="250px" height="250px">
                        </div>
                        <div style="display:inline-block;">
                            <h3 class="text-center fw-bold pt-2 text-white">Anjana</h3>
                            <hr class=" " style="height:5px; background-color:#fff; margin-top:-5px;">
                            <h5 class="text-center text-white" style="margin-top:-9px;">CNC Trainer</h5>
                        </div>
                    </div>
                    <div class="col-lg-4 col-12 col-sm-6mb-lg-0 mb-5">
                        <div>
                            <img src="images/Hari-sir.jpg" width="250px" height="250px">
                        </div>
                        <div style="display:inline-block;">
                            <h3 class="text-center fw-bold pt-2 text-white">Harikrishnan</h3>
                            <hr class=" " style="height:5px; background-color:#fff; margin-top:-5px;">
                            <h5 class="text-center text-white" style="margin-top:-9px;">SM Trainer</h5>
                        </div>
                    </div>
                    <div class="col-lg-4 col-12 col-sm-6mb-lg-0 mb-5">
                        <div>
                            <img src="swapna.jpeg" width="250px" height="250px">
                        </div>
                        <div style="display:inline-block;">
                            <h3 class="text-center fw-bold pt-2 text-white">Swapna</h3>
                            <hr class=" " style="height:5px; background-color:#fff; margin-top:-5px;">
                            <h5 class="text-center text-white" style="margin-top:-9px;">English Trainer</h5>
                        </div>
                    </div>
                </div>
            </div>
     </section>

           <footer class="pt-5 pt-5 mt-5 mb-0">
              <div class="container-fluid container-md " >
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
    <script>
        function btn2(){
            document.getElementById('div-1').style.display="none";
            document.getElementById('div-2').style.display="block";
            document.getElementById('div-3').style.display="none";
        }
        function btn3(){
            document.getElementById('div-1').style.display="none";
            document.getElementById('div-2').style.display="none";
            document.getElementById('div-3').style.display="block";
        }
        function btn1(){
            document.getElementById('div-1').style.display="block";
            document.getElementById('div-2').style.display="none";
            document.getElementById('div-3').style.display="none";
        }
    </script>

</body>
</html>
""")