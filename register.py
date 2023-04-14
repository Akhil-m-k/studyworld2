#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

print("""
    <html>
    <head>
     <style>
        /* Modal */

           /* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index:500; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content/Box */
.modal-content {
  background-color: #fefefe;
  margin: auto; /* Center the modal */
  padding: 20px;
  border: 1px solid #888;
  width: 30%; /* Could be more or less, depending on screen size */
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
   box-shadow:0px 0px 15px rgba(0,0,0,0.5);
  border-radius: 10px;
}

/* The Close Button */
.close {
  color: #aaa;
  position:absolute;
  right:15px;
  top:10px;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

/* Blur the background when the modal is open */
body.modal-open {
  overflow: hidden;
}
.modal form{
  padding: 20px;

}

.modal input{
  width: 100%;
  margin-bottom: 20px;
  height: 45px;
  border: 1px solid gray;
  border-radius: 5px;
  font-size: 18px;
  padding-left: 10px;
}
.modal select{
  width: 103%;
  margin-bottom: 20px;
  height: 45px;
  border: 1px solid gray;
  border-radius: 5px;
  font-size: 18px;
  padding-left: 10px;
}

.modal input:focus{
  outline: none;
}

.modal label{
  text-align: start;
  font-size: 21px;
  font-weight: bold;
}
.modal h2{
  text-align: center;
  margin-top:25px;
}
.modal form input[type="submit"]{
  width: 40%;
  background-color: orange;
  border: none;
  border-radius: 5px;
  color:black;
  font-size: 20px;
  font-weight: bold;
  height: 40px;
  margin-left: 30%;
}
@media (max-width:1300px){
  .modal-content {
    width:50%;
  }
}
@media (max-width:550px){
  .modal-content {
    width:80%;
  }
}
     </style>
    </head>
    <body>
      <!-- Modal -->
        <div id="loginModal" class="modal">
    <div class="modal-content">
      <span class="close">&times;</span>
      <h2>REGISTRATION FOR COURSE</h2>
      <form>
        <label for="username">Full Name </label>
        <input type="text" id="username" name="username" placeholder="Enter your name"><br>

        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Enter your email"><br>

        <label for="phone">Mobile</label>
        <input type="tel" id="phone" name="phone" placeholder="Enter your phone number"><br>

        <label for="phone">Select Course</label>
        <select name="course" id="course">
          <option value="">select course</option>
          <option value="B.E Mechanical Engineering">B.E Mechanical Engineering</option>
          <option value="B.E Electronics and Communication Engineering">B.E Electronics and Communication Engineering</option>
          <option value="B.E Electrical and Electronics Engineering">B.E Electrical and Electronics Engineering</option>
          <option value="B.E Computerscience and Engineering">B.E Computerscience and Engineering</option>
        </select>

        <input type="submit" value="Register">
      </form>
    </div>
  </div>
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
""")