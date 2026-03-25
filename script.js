document.getElementById("feedbackForm").addEventListener("submit", function(e) {

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let mobile = document.getElementById("mobile").value.trim();
    let dept = document.getElementById("department").value;
    let feedback = document.getElementById("feedback").value.trim();
    let gender = document.querySelector('input[name="gender"]:checked');
    let error = document.getElementById("error");

    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

    if(name === ""){
        error.innerText = "Name cannot be empty";
        e.preventDefault();
        return;
    }

    if(!email.match(emailPattern)){
        error.innerText = "Invalid Email";
        e.preventDefault();
        return;
    }

    if(!/^\d{10}$/.test(mobile)){
        error.innerText = "Invalid Mobile Number";
        e.preventDefault();
        return;
    }

    if(!gender){
        error.innerText = "Select Gender";
        e.preventDefault();
        return;
    }

    if(dept === ""){
        error.innerText = "Select Department";
        e.preventDefault();
        return;
    }

    if(feedback.split(" ").length < 10){
        error.innerText = "Feedback must contain at least 10 words";
        e.preventDefault();
        return;
    }

    alert("Form submitted successfully!");
});